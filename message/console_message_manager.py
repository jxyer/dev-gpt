from message.message_manager import MessageManager


class ConsoleMessageManager(MessageManager):

    async def recv(self) -> str:
        return input("请输出消息：")

    async def send(self, message):
        print(message)
