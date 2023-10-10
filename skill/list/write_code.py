from agent import Message, EXTRA_TYPE_NONE
from config.project_config import project
from context import ProjectContext
from prompt.prompt import Prompt
from skill.list.interrupt_skill import InterruptSkill
from skill.list.skill import send_robot_message


class WriteCode(InterruptSkill):
    FLAG = '写代码'

    def describe(self) -> str:
        return """当需要写代码时选择这个技能"""

    async def act(self, message_manager) -> Message:
        result = self.llm.chat_result(
            project['stream'],
            Prompt.responsibility(),
            Prompt.Skill.write_code()
        )
        return await send_robot_message(message_manager, result, EXTRA_TYPE_NONE, [])
