from agent import Message, EXTRA_TYPE_NONE
from config.project_config import project
from context import ProjectContext
from prompt.prompt import Prompt
from .code_interpreter import CodeInterpreter
from .skill import send_robot_message


class CreateMenu(CodeInterpreter):
    FLAG = '创建目录'

    def describe(self) -> str:
        return "当需要创建目录、文件时选择这个技能。"

    async def act(self, messageManager) -> Message:
        self.interpreter.reset()
        result = self.interpreter.chat(Prompt.created_menu(plan=ProjectContext.cur_plan,
                                                           project_path=project['project_path']), True)
        return await send_robot_message(messageManager, f"已经成功执行创建目录${result[-1]['content']}", EXTRA_TYPE_NONE, [])
