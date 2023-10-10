from agent.qa import QA


class ProjectContext:
    requirement: str
    cur_plan: str
    detail_requirement: list[QA] = []

    @staticmethod
    def format_detail_requirement() -> list[str]:
        if ProjectContext.detail_requirement is None:
            return []
        return [f"{item.question}\n{item.answer}" for item in ProjectContext.detail_requirement]
