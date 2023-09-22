from agent import Message, EXTRA_TYPE_NONE
from config.project_config import project
from context import MessageContext
from prompt import Prompt
from skill.interrupt_skill.interrupt_skill import InterruptSkill
from skill.skill import send_robot_message


class WriteCode(InterruptSkill):
    FLAG = '写代码'

    def describe(self) -> str:
        return """当需要写代码时选择这个技能"""

    async def act(self, ws) -> Message:
        result = self.llm.chat_result(
            project['stream'],
            Prompt.responsibility(),
            Prompt.Skill.write_code(message_record=[f"{m.profile}说：{m.content}" for m in MessageContext.message_record])
        )
        return await send_robot_message(ws, result, EXTRA_TYPE_NONE, [])
