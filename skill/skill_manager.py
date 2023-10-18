from agent import Message
from message.message_manager import MessageManager
from skill.list.create_menu import CreateMenu
from skill.list.inquire import Inquire
from skill.list.make_plan import MakePlan
from skill.list.run_code import RunCode
from skill.list.web_analytics import WebAnalytics
from skill.list.write_code import WriteCode


class SkillManager:
    skill_dict = {
        Inquire.FLAG: Inquire(),
        WebAnalytics.FLAG: WebAnalytics(),
        WriteCode.FLAG: WriteCode(),
        CreateMenu.FLAG: CreateMenu(),
        RunCode.FLAG: RunCode(),
        MakePlan.FLAG: MakePlan(),
    }

    @staticmethod
    async def useSkill(messageManager: MessageManager, skill_name: str) -> Message:
        skill = SkillManager.skill_dict.get(skill_name)
        result = await skill.act(messageManager)
        return result

    @staticmethod
    def get_skills_name() -> list[str]:
        return list(SkillManager.skill_dict.keys())

    @staticmethod
    def get_skills_describes() -> list[str]:
        skill_describes = []
        for key, value in SkillManager.skill_dict.items():
            skill_describes.append(f"{key}:{value.describe()}")
        return skill_describes
