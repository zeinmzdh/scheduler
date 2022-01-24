
class Task:
    def __init__(self, name, task_type, duration, arrival_time):
        self.name = name
        self.task_type = task_type
        self.duration = float(duration)
        self.time_left = float(duration)
        self.time_completed = 0
        self. arrival_time = float(arrival_time)
        self.waiting_time = 0
        self.response_ratio = (self.duration + self.waiting_time) / self.duration

    def has_time_left(self):
        if self.time_left > 0:
            return True
        return False

    def update_waiting_time_and_rr_time(self, curr_time):
        self.waiting_time = curr_time - self.arrival_time
        # print(self.waiting_time)
        self.response_ratio = (self.duration + self.waiting_time) / self.duration
        # print(self.response_ratio,  (self.duration + self.waiting_time) / self.duration)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

