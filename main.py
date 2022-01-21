from task import Task

if __name__ == '__main__':
    tasks_count = int(input())
    tasks = []
    for i in range(tasks_count):
        n, t, d = input().split()
        task = Task(n, t, d)
        tasks.append(task)


def first_come_first_served(tasks_list):
    pass


def shortest_job_first(tasks_list):
    pass


def round_robin(tasks_list):
    pass


def highest_response_ratio_first(tasks_list):
    pass

