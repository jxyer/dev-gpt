from message.message import Message


class WebSocketMessage(Message):
    def recv(self) -> str:
        return "没有实现"

    def send(self, message):
        pass
