from agent import Message
from config.project_config import project
from context import MessageContext
from prompt import Prompt
from .skill import Skill


class Learn(Skill):
    FLAG = "学习"

    async def act(self, messageManager) -> Message | str:
        schema = {

        }
        result = self.llm.chat_result(
            project['stream'],
            Prompt.responsibility(),
            Prompt.is_know(message_record=MessageContext.format_message())
        )
        return result

    def describe(self) -> str:
        return "学习"
