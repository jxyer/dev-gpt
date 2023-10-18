from pydantic.v1 import BaseModel, Field


class CheckPlanSchema(BaseModel):
    """检测任务是否完成"""

    is_finish: bool = Field(..., description="检测计划是否已经完成")
