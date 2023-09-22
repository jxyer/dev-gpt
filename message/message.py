import abc


class Message:

    @abc.abstractmethod
    def recv(self) -> str:
        """
        接收消息
        :return:
        """

    @abc.abstractmethod
    def send(self, message):
        """
        发送消息
        :return:
        """
