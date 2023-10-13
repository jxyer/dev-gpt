from agent import Message
from agent.plan import PlanSchema
from context import ProjectContext
from prompt.prompt import Prompt
from .skill import Skill


class MakePlan(Skill):
    FLAG = "制定计划"

    async def act(self, message_manager) -> Message | str:
        result = self.llm.structured_output(
            PlanSchema,
            Prompt.responsibility(),
            Prompt.make_plan(ProjectContext.requirement)
        )
        return result

    def describe(self) -> str:
        return "规划代码流程"
