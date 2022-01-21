from task import Task


def first_come_first_served(tasks_list):
    time = 0
    while len(tasks_list) != 0 :
        running_task = tasks_list.pop(0)
        while running_task.has_time_left():
            print('t:', time, 'running task:', running_task, 'seconds_passed:', running_task.time_completed,
                  'time_left:', running_task.time_left)
            print('ready list:', tasks_list)
            if running_task.time_left >= 1:
                time = time + 1
                running_task.time_left = running_task.time_left - 1
                running_task.time_completed = running_task.time_completed + 1
            else:
                time = time + running_task.time_left
                running_task.time_left = running_task.time_left - running_task.time_left
                running_task.time_completed = running_task.time_completed + running_task.time_left
        print('-------------------------------------------------------------')

        print('t:', time, 'task_completed:', running_task, 'seconds_passed:', running_task.time_completed)
        print('-------------------------------------------------------------')


def shortest_job_first(tasks_list):
    tasks_list.sort(key=lambda x: x.duration)
    print(tasks_list)
    time = 0
    while len(tasks_list) != 0:
        running_task = tasks_list.pop(0)
        while running_task.has_time_left():
            print('t:', time, 'running task:', running_task, 'seconds_passed:', running_task.time_completed,
                  'time_left:', running_task.time_left)
            print('ready list:', tasks_list)
            if running_task.time_left >= 1:
                time = time + 1
                running_task.time_left = running_task.time_left - 1
                running_task.time_completed = running_task.time_completed + 1
            else:
                time = time + running_task.time_left
                running_task.time_left = running_task.time_left - running_task.time_left
                running_task.time_completed = running_task.time_completed + running_task.time_left
        print('-------------------------------------------------------------')

        print('t:', time, 'task_completed:', running_task, 'seconds_passed:', running_task.time_completed)
        print('-------------------------------------------------------------')
    pass


def round_robin(tasks_list):
    pass


def highest_response_ratio_first(tasks_list):
    pass


if __name__ == '__main__':
    tasks_count = int(input())
    tasks = []
    for i in range(tasks_count):
        n, t, d = input().split()
        task = Task(n, t, d)
        tasks.append(task)

    shortest_job_first(tasks)

