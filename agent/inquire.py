from pydantic.v1 import BaseModel, Field
from typing import Sequence


class InquireSchema(BaseModel):
    """询问"""

    question: Sequence[str] = Field(..., description="对用户的需求进行问题")
