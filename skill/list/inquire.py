from agent import Message, EXTRA_TYPE_LIST
from agent.inquire import InquireSchema
from agent.qa import QA
from context.project_context import ProjectContext

from prompt.prompt import Prompt
from .skill import Skill, send_robot_message


class Inquire(Skill):
    FLAG = '询问'

    def describe(self) -> str:
        return "当你对用户需求不明确时，可以选择这个功能。"

    async def act(self, message_manager) -> Message:
        result = self.llm.structured_output(
            InquireSchema,
            Prompt.responsibility(),
            Prompt.Skill.inquire(requirement=ProjectContext.requirement)
        )
        for question in result.question:
            await message_manager.send(question)
            answer = await message_manager.recv()
            ProjectContext.detail_requirement.append(QA(question, answer))
        return await send_robot_message(message_manager,
                                        "",
                                        EXTRA_TYPE_LIST,
                                        ProjectContext.format_detail_requirement())
