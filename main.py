from task import Task


def first_come_first_served(tasks_list):
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


def shortest_job_first(tasks_list):
    tasks_list.sort(key=lambda x: x.duration)
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


def round_robin(tasks_list):
    q = 0.5
    time = 0
    while len(tasks_list) != 0:
        running_task = tasks_list.pop(0)
        print('t:', time, 'running task:', running_task, 'seconds_passed:', running_task.time_completed,
              'time_left:', running_task.time_left)
        print('ready list:', tasks_list)
        if running_task.time_left >= q:
            time = time + q
            running_task.time_left = running_task.time_left - q
            running_task.time_completed = running_task.time_completed + q
        else:
            time = time + running_task.time_left
            running_task.time_left = running_task.time_left - running_task.time_left
            running_task.time_completed = running_task.time_completed + running_task.time_left
        if not running_task.has_time_left():
            print('-------------------------------------------------------------')
            print('t:', time, 'task_completed:', running_task, 'seconds_passed:', running_task.time_completed)
            print('-------------------------------------------------------------')
        else:
            tasks_list.append(running_task)


def highest_response_ratio_next(tasks_list):
    time = 0
    ready_list = []
    ready_list = ready_list + check_for_new_tasks(tasks_list, time)
    while len(ready_list) != 0:
        running_task = ready_list.pop(0)
        while running_task.has_time_left():
            ready_list = ready_list + check_for_new_tasks(tasks_list, time)
            for tsk in ready_list:
                tsk.update_waiting_time_and_rr_time(time)
            ready_list.sort(key=lambda x: x.response_ratio)
            print('t:', time, 'running task:', running_task, 'seconds_passed:', running_task.time_completed,
                  'time_left:', running_task.time_left)
            print('ready list:', ready_list)
            if running_task.time_left >= 1:
                time = time + 1
                running_task.time_left = running_task.time_left - 1
                running_task.time_completed = running_task.time_completed + 1
            else:
                time = time + running_task.time_left
                running_task.time_left = running_task.time_left - running_task.time_left
                running_task.time_completed = running_task.time_completed + running_task.time_left

        ready_list = ready_list + check_for_new_tasks(tasks_list, time)
        for tsk in ready_list:
            tsk.update_waiting_time_and_rr_time(time)
        ready_list.sort(key=lambda x: x.response_ratio)
        # for x in ready_list:
        #     print(x.name, ": ", x.response_ratio)
        # print(ready_list)
        print('-------------------------------------------------------------')
        print('t:', time, 'task_completed:', running_task, 'seconds_passed:', running_task.time_completed)
        print('ready list:', ready_list)
        print('-------------------------------------------------------------')


def check_for_new_tasks(tasks_list, curr_time):
    tmp = []
    for i, tsk in enumerate(tasks_list):
        if tsk.arrival_time <= curr_time:
            tmp.append(tsk)
            tasks_list.pop(i)
    return tmp


if __name__ == '__main__':
    tasks_count = int(input())
    tasks = []
    for i in range(tasks_count):
        n, t, d = input().split()
        task = Task(n, t, d, i)
        tasks.append(task)

    highest_response_ratio_next(tasks)
