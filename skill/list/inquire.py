from agent.inquire import InquireSchema
from agent.qa import QA
from context.project_context import ProjectContext

from prompt.prompt import Prompt
from .skill import Skill


class Inquire(Skill):
    FLAG = '询问'

    def describe(self) -> str:
        return "当你对用户需求不明确时，可以选择这个功能。"

    async def act(self, messageManager) -> list[QA]:
        result = self.llm.structured_output(
            InquireSchema,
            Prompt.responsibility(),
            Prompt.Skill.inquire(requirement=ProjectContext.requirement)
        )
        qa: list[QA] = []
        for question in result.question:
            await messageManager.send(question)
            answer = await messageManager.recv()
            qa.append(QA(question, answer))
            print('qa', qa)
        ProjectContext.detailRequirement = qa
        return qa
