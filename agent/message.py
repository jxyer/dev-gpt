import uuid

from pydantic import BaseModel

EXTRA_TYPE_NONE = 0
EXTRA_TYPE_LIST = 1
EXTRA_TYPE_FORM = 2


class Message(BaseModel):
    # 消息id:
    message_id: str
    # 身份
    profile: str
    # 对话内容
    content: str
    # 额外数据类型
    extra_type: int
    # 额外数据
    extra_data: list

    def __init__(self, message_id: str, profile: str, content: str, extra_type: int, extra_data: list):
        super().__init__(message_id=message_id,
                         profile=profile,
                         content=content,
                         extra_type=extra_type,
                         extra_data=extra_data)

    @staticmethod
    def generate_id() -> str:
        """
        生成id
        :return:
        """
        return str(uuid.uuid1())
