from context.project_context import ProjectContext
from skill.list.make_plan import MakePlan
from skill.list.think import Think
from skill.skill_manager import SkillManager


class TaskPlanner:
    def __init__(self, message_manager):
        self.message_manager = message_manager

    async def make_plan(self):
        # 根据用户需求生成任务计划的代码，并返回任务计划列表
        result = await SkillManager.useSkill(self.message_manager, MakePlan.FLAG)
        return result

    async def execute_plan(self, plans):
        for plan in plans:
            # 执行任务计划的代码
            ProjectContext.cur_plan = plan
            # 思考计划使用什么功能
            skill_name = await SkillManager.useSkill(self.message_manager, Think.FLAG)
            # 执行技能
            await SkillManager.useSkill(self.message_manager, skill_name)
