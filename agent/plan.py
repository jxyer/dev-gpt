from typing import Sequence

from pydantic.v1 import BaseModel, Field


class PlanSchema(BaseModel):
    """ 思考使用什么技能合适 """

    plans: Sequence[str] = Field(..., description="计划列表详情")
