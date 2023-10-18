from agent import Message, EXTRA_TYPE_LIST
from agent.plan import PlanSchema
from context import ProjectContext
from prompt.prompt import Prompt
from .skill import Skill, send_robot_message


class MakePlan(Skill):
    FLAG = "制定计划"

    async def act(self, message_manager) -> Message:
        result = self.llm.structured_output(
            PlanSchema,
            Prompt.responsibility(),
            Prompt.make_plan(ProjectContext.requirement)
        )
        return await send_robot_message(message_manager, "", EXTRA_TYPE_LIST, result.plans)

    def describe(self) -> str:
        return "规划代码流程"
