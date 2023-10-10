import abc

from agent import Message
from config.project_config import llms, cur_llm
from llm.llm import LLM
from message.message_manager import MessageManager


class Skill:
    def __init__(self):
        self.llm: LLM = llms.get(cur_llm)

    @abc.abstractmethod
    async def act(self, message_manager: MessageManager) -> Message | str:
        """
        由子类实现，执行技能
        :return:
        """

    @abc.abstractmethod
    def describe(self) -> str:
        """
        skill descript
        :return:
        """


async def send_robot_message(message_manager: MessageManager, message, extra_type, extra_data) -> Message:
    m = Message(message_id=Message.generate_id(),
                profile='Robot',
                content=message,
                extra_type=extra_type,
                extra_data=extra_data)
    await message_manager.send(m.model_dump_json())
    return m


async def send_system_message(message_manager: MessageManager, message, extra_type, extra_data) -> Message:
    m = Message(message_id=Message.generate_id(),
                profile='System',
                content=message,
                extra_type=extra_type,
                extra_data=extra_data)
    await message_manager.send(m.model_dump_json())
    return m
