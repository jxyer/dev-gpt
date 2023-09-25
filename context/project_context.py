from agent.qa import QA


class ProjectContext:
    requirement: str
    cur_plan: str
    detailRequirement: list[QA]
