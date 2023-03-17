from models.guide_task import GuideTask


class Guide:
    def __init__(self, name: str):
        self.tasks = []
        self.name = name

    def add_task(self, task: GuideTask) -> None:
        self.tasks.append(task)
