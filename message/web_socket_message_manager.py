from message.message_manager import MessageManager


class WebSocketMessageManager(MessageManager):
    async def recv(self) -> str:
        return "没有实现"

    async def send(self, message):
        pass
