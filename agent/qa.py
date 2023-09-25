from pydantic import BaseModel


class QA(BaseModel):
    question: str
    answer: str

    def __init__(self, question: str, answer: str):
        super().__init__(question=question,
                         answer=answer)
