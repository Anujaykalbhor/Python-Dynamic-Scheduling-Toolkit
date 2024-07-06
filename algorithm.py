def fcfs_dynamic(processes, timeline, finish_time, turn_around_time, norm_turn, last_instant):
    time = 0
    queue = []
    current_process = None

    for current_time in range(last_instant):
        for process in processes:
            if process[1] == current_time:
                queue.append(process)

        if current_process is None and queue:
            current_process = queue.pop(0)
            start_time = current_time

        if current_process:
            process_index = processes.index(current_process)
            if current_time < last_instant and process_index < len(timeline[0]):
                timeline[current_time][process_index] = '*'
            if current_time - start_time + 1 == current_process[2]:
                finish_time[process_index] = current_time + 1
                turn_around_time[process_index] = finish_time[process_index] - current_process[1]
                norm_turn[process_index] = turn_around_time[process_index] / current_process[2]
                current_process = None

    return timeline, finish_time, turn_around_time, norm_turn

def round_robin_dynamic(processes, quantum, last_instant):
    timeline = [[' ' for _ in range(len(processes))] for _ in range(last_instant)]
    finish_time = [0] * len(processes)
    turn_around_time = [0] * len(processes)
    norm_turn = [0] * len(processes)

    queue = []
    remaining_time = {p[0]: p[2] for p in processes}
    current_time = 0

    while current_time < last_instant:
        for process in processes:
            if process[1] == current_time:
                queue.append(process)

        if queue:
            process = queue.pop(0)
            process_index = [i for i, p in enumerate(processes) if p[0] == process[0]][0]
            for t in range(min(quantum, remaining_time[process[0]])):
                if current_time < last_instant and process_index < len(timeline[0]):
                    timeline[current_time][process_index] = '*'
                current_time += 1
                remaining_time[process[0]] -= 1
                if remaining_time[process[0]] == 0:
                    finish_time[process_index] = current_time
                    turn_around_time[process_index] = finish_time[process_index] - process[1]
                    norm_turn[process_index] = turn_around_time[process_index] / process[2]
                    break
            else:
                queue.append(process)
            current_time -= 1

        current_time += 1

    return timeline, finish_time, turn_around_time, norm_turn
