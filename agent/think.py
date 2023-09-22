from pydantic.v1 import BaseModel, Field


class ThinkSchema(BaseModel):
    """ 思考使用什么技能合适 """

    skill: str = Field(..., description="使用的技能")
    reason: str = Field(..., description="为什么选择使用这个技能")