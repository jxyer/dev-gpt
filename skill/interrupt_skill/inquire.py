from agent import Message, EXTRA_TYPE_FORM
from agent.inquire import InquireSchema
from context import MessageContext
from prompt import Prompt
from .interrupt_skill import InterruptSkill
from ..skill import send_robot_message


class Inquire(InterruptSkill):
    FLAG = '询问'

    def describe(self) -> str:
        return "当你对用户需求不明确时，可以选择这个功能。"

    async def act(self, ws) -> Message:
        result = self.llm.structured_output(
            InquireSchema,
            Prompt.responsibility(),
            Prompt.Skill.inquire(requirement=MessageContext.message_record[0],
                                 message_record=MessageContext.format_message())
        )
        print('result.question', result.question)
        question_message = await send_robot_message(ws, "", EXTRA_TYPE_FORM, result.question)
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
