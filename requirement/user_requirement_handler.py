from config.project_config import project
from exception.project_exception import ProjectException
from message.console_message import ConsoleMessage
from message.message import Message
from message.web_socket_message import WebSocketMessage
from requirement.task_planner import TaskPlanner


class UserRequirementHandler:
    def __init__(self):
        self.project = project
        self.message: Message = self._create_message()

    def _create_message(self):
        if self.project.get('user_message') == 'console':
            return ConsoleMessage()
        elif self.project.get('user_message') == 'websocket':
            return WebSocketMessage()
        else:
            raise ProjectException(f'The key "user_message" is not found in the project dictionary. '
                                   f'The key should be present when the project is initialized. '
                                   f'Project dictionary: {project}')

    def get_user_requirement(self):
        return self.message.recv()

    def handle_user_requirement(self, requirement):
        # 询问具体要求
        requirement = self.inquire_requirement(requirement)

        taskPlanner = TaskPlanner(requirement)
        # 根据用户需求列出任务计划
        plans = taskPlanner.make_plan()
        # 执行任务计划
        taskPlanner.execute_plan(plans)

    def sendHandleResult(self, handle_result):
        pass

    def inquire_requirement(self, requirement):

        return ''
