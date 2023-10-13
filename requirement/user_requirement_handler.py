from config.project_config import project
from context.project_context import ProjectContext
from exception.project_exception import ProjectException
from message.console_message_manager import ConsoleMessageManager
from message.message_manager import MessageManager
from message.web_socket_message_manager import WebSocketMessageManager
from requirement.task_planner import TaskPlanner
from skill.list.inquire import Inquire
from skill.skill_manager import SkillManager


class UserRequirementHandler:
    def __init__(self):
        self.project = project
        self.message_manager: MessageManager = self._create_message()

    def _create_message(self):
        if self.project.get('user_message') == 'console':
            return ConsoleMessageManager()
        elif self.project.get('user_message') == 'websocket':
            return WebSocketMessageManager()
        else:
            raise ProjectException(f'The key "user_message" is not found in the project dictionary. '
                                   f'The key should be present when the project is initialized. '
                                   f'Project dictionary: {project}')

    async def get_user_requirement(self):
        return await self.message_manager.recv()

    async def handle_user_requirement(self, requirement):
        ProjectContext.requirement = requirement
        # 询问具体要求
        ProjectContext.detail_requirement = await self.inquire_requirement()
        # pop历史记录
        taskPlanner = TaskPlanner(self.message_manager)
        # 根据用户需求定制代码计划
        plans = await taskPlanner.make_plan()
        for plan in plans:
            # 执行代码计划
            plan_result = await taskPlanner.execute_plan(plan)
            # 人工检测
            await taskPlanner.human_review(plan_result)

    def sendHandleResult(self, handle_result):
        pass

    async def inquire_requirement(self):
        # 使用询问技能
        result = await SkillManager.useSkill(self.message_manager, Inquire.FLAG)
        return result
