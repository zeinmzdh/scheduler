
class Task:
    def __init__(self, name, task_type, duration):
        self.name = name
        self.task_type = task_type
        self.duration = float(duration)
        self.time_left = float(duration)
        self.time_completed = 0

    def has_time_left(self):
        if self.time_left > 0:
            return True
        return False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

