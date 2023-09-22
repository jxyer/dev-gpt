from pydantic.v1 import BaseModel, Field


class CheckTaskSchema(BaseModel):
    """检测任务是否完成"""

    is_finish: bool = Field(..., description="任务是否已经完成")
