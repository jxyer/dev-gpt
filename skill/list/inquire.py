from agent import Message
from agent.inquire import InquireSchema
from context.project_context import ProjectContext

from prompt.prompt import Prompt
from .skill import Skill


class Inquire(Skill):
    FLAG = '询问'

    def describe(self) -> str:
        return "当你对用户需求不明确时，可以选择这个功能。"

    async def act(self, messageManager) -> Message:
        result = self.llm.structured_output(
            InquireSchema,
            Prompt.responsibility(),
            Prompt.Skill.inquire(requirement=ProjectContext.requirement)
        )
        question_message = await messageManager.send(result)
        """
        qa_json: 
        [{
            "question":"question",
            "answer":"answer"
        },...]
        """
        qa_json = await ws.recv()
        print("qa_json", qa_json)

        return question_message
