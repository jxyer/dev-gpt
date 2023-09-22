from message.message import Message


class ConsoleMessage(Message):

    def recv(self) -> str:
        return input("请输出消息：")

    def send(self, message):
        print(message)
