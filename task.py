
class Task:
    def __init__(self, name, task_type, duration):
        self.name = name
        self.task_type = task_type
        self.duration = duration
        self.time_left = duration
        self.time_completed = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

