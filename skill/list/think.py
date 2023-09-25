from agent import EXTRA_TYPE_LIST, EXTRA_TYPE_NONE
from agent.think import ThinkSchema
from context import ProjectContext
from prompt.prompt import Prompt
from .skill import Skill, send_system_message, send_robot_message
from ..skill_manager import SkillManager


class Think(Skill):
    FLAG = '思考'

    def describe(self) -> str:
        pass

    async def act(self, messageManager) -> str:
        """
        返回使用技能名称
        :param messageManager:
        :return: 技能名称
        """
        skills = SkillManager.get_skills_name()
        result = self.llm.structured_output(
            ThinkSchema,
            Prompt.responsibility(),
            Prompt.think(
                requirement=ProjectContext.cur_plan,
                skills=skills, skills_describes=SkillManager.get_skills_describes())
        )
        await send_robot_message(messageManager, result.reason, EXTRA_TYPE_NONE, [])
        if result.skill in skills:
            skill_name = result.skill
        else:
            hint = f"请根据上面描述，选择一个合适技能让ai去使用。"
            await send_system_message(messageManager, hint, EXTRA_TYPE_LIST, skills)
            skill_name = await messageManager.recv()
        return skill_name
