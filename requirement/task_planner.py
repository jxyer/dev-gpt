from config.project_config import project
from context.project_context import ProjectContext
from llm.gpt import GPT
from prompt.prompt import Prompt
from skill.list.make_plan import MakePlan
from skill.list.think import Think
from skill.list.write_code import WriteCode
from skill.skill_manager import SkillManager


class TaskPlanner:
    def __init__(self, message_manager):
        self.message_manager = message_manager

    async def make_plan(self):
        # 根据用户需求生成任务计划的代码，并返回任务计划列表
        result = await SkillManager.useSkill(self.message_manager, MakePlan.FLAG)
        print("执行计划：", result)
        return result

    async def execute_plan(self, plan):
        # 执行任务计划的代码
        ProjectContext.cur_plan = plan
        print("当前计划：", plan)
        # 思考计划使用什么功能
        skill_name = await Think().act(self.message_manager)
        print("使用技能：", skill_name)
        # 执行技能
        result = await SkillManager.useSkill(self.message_manager, skill_name)
        return result

    async def human_review(self, plan_result):
        gpt = GPT()
        message_record = [Prompt.AIMessage(plan_result)]
        while True:
            message = self.message_manager.recv()
            if message == 'end':
                break
            message_record.append(Prompt.HumanMessage(message))
            result = gpt.chat_result(project['stream'], *message_record)
            message_record.append(Prompt.AIMessage(result))
