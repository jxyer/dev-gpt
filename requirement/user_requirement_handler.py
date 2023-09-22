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

    def get_user_requirement(self):
        return self.message_manager.recv()

    async def handle_user_requirement(self, requirement):
        ProjectContext.requirement = requirement
        # 询问具体要求
        requirement = await self.inquire_requirement()

        taskPlanner = TaskPlanner(self.message_manager, requirement)
        # 根据用户需求列出任务计划
        plans = taskPlanner.make_plan()
        # 执行任务计划
        taskPlanner.execute_plan(plans)

    def sendHandleResult(self, handle_result):
        pass

    async def inquire_requirement(self):
        # 使用询问技能
        result = await SkillManager.useSkill(self.message_manager, Inquire.FLAG)
        return result
