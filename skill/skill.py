import abc

from agent import Message
from config.project_config import llms, cur_llm
from llm.llm import LLM


class Skill:
    def __init__(self):
        self.llm: LLM = llms.get(cur_llm)

    @abc.abstractmethod
    async def act(self, ws) -> Message | str:
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


async def send_robot_message(ws, message, extra_type, extra_data) -> Message:
    m = Message(message_id=Message.generate_id(),
                profile='Robot',
                content=message,
                extra_type=extra_type,
                extra_data=extra_data)
    await ws.send(m.model_dump_json())
    return m


async def send_system_message(ws, message, extra_type, extra_data) -> Message:
    m = Message(message_id=Message.generate_id(),
                profile='System',
                content=message,
                extra_type=extra_type,
                extra_data=extra_data)
    await ws.send(m.model_dump_json())
    return m
