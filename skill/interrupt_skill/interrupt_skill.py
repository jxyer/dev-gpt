from abc import ABC

from skill.skill import Skill


class InterruptSkill(Skill, ABC):
    """
    可以中断的技能
    """
    pass
