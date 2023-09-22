import abc


class LLM:
    def __init__(self):
        pass

    @abc.abstractmethod
    def chat_result(self, stream: bool, *messages: object):
        """
        返回聊天结果
        :return:
        """

    @abc.abstractmethod
    def structured_output(self, schema, *messages: object) -> any:
        """
        结构化输出
        :return:
        """