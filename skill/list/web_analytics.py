from .skill import Skill


class WebAnalytics(Skill):
    FLAG = '网页分析'

    def describe(self) -> str:
        return "可以对网页进行分析，当你有不懂的知识时可以选择这个。"

    async def act(self, messageManager) -> str:
        pass
