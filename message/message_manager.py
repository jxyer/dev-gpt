import abc


class MessageManager:

    @abc.abstractmethod
    async def recv(self) -> str:
        """
        接收消息
        :return:
        """

    @abc.abstractmethod
    async def send(self, message):
        """
        发送消息
        :return:
        """
