from agent import EXTRA_TYPE_NONE, Message
from agent.check_plan import CheckPlanSchema
from config.project_config import project, llms, cur_llm
from context.project_context import ProjectContext
from llm.gpt import GPT
from prompt.prompt import Prompt
from skill.list.make_plan import MakePlan
from skill.list.think import Think
from skill.skill_manager import SkillManager


class TaskPlanner:
    def __init__(self, message_manager):
        self.message_manager = message_manager

    async def make_plan(self):
        # 根据用户需求生成任务计划的代码，并返回任务计划列表
        result = await SkillManager.useSkill(self.message_manager, MakePlan.FLAG)
        print("执行计划：", result.extra_data)
        return result.extra_data

    async def execute_plan(self, plan) -> Message:
        # 执行任务计划的代码
        ProjectContext.cur_plan = plan
        print("当前计划：", plan)
        # 思考计划使用什么功能
        skill_name = await Think().act(self.message_manager)
        print("使用技能：", skill_name)
        # 执行技能
        skill_result = await SkillManager.useSkill(self.message_manager, skill_name)
        # 获取执行技能结果
        plan_result = skill_result.content if EXTRA_TYPE_NONE == skill_result.extra_type else skill_result.extra_data
        if await self.check_plan(plan, plan_result):
            return skill_result
        else:
            return await self.execute_plan(plan)

    @staticmethod
    async def check_plan(plan, plan_result):
        llm = llms.get(cur_llm)
        result = llm.structured_output(CheckPlanSchema,
                                       Prompt.responsibility(),
                                       Prompt.check_plan(plan, plan_result))
        return result.is_finish

    async def human_review(self, plan_result: Message):
        gpt = GPT()
        message_record = [Prompt.AIMessage(
            plan_result.content if plan_result.extra_type == EXTRA_TYPE_NONE else str(plan_result.extra_data))]
        while True:
            message = await self.message_manager.recv()
            if message == 'end':
                break
            message_record.append(Prompt.HumanMessage(message))
            result = gpt.chat_result(project['stream'], *message_record)
            await self.message_manager.send(result)
            message_record.append(Prompt.AIMessage(result))
