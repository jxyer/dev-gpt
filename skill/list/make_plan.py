from agent import Message
from config.project_config import project
from context import ProjectContext
from prompt.prompt import Prompt
from .skill import Skill


class MakePlan(Skill):
    FLAG = "制定计划"

    async def act(self, messageManager) -> Message | str:
        result = self.llm.chat_result(
            project['stream'],
            Prompt.responsibility(),
            Prompt.make_plan(ProjectContext.requirement)
        )
        return result

    def describe(self) -> str:
        return "规划代码流程"
