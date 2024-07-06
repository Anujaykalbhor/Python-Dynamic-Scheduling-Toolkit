def clear_timeline(last_instant, process_count):
    return [[' ' for _ in range(process_count)] for _ in range(last_instant)]

def print_timeline(timeline, process_names):
    for t in range(len(timeline)):
        print(f"{t % 10} ", end="")
    print("\n" + "-" * (2 * len(timeline)) + "\n")
    for i, process_name in enumerate(process_names):
        print(f"{process_name} |", end="")
        for t in range(len(timeline)):
            print(timeline[t][i] + "|", end="")
        print("\n")
    print("-" * (2 * len(timeline)))

def print_stats(processes, finish_time, turn_around_time, norm_turn):
    process_count = len(processes)
    print("Process    ", end="")
    for process in processes:
        print(f"|  {process[0]}  ", end="")
    print("|\n")

    print("Arrival    ", end="")
    for process in processes:
        print(f"|{process[1]:3}  ", end="")
    print("|\n")

    print("Service    |", end="")
    for process in processes:
        print(f"{process[2]:3}  |", end="")
    print(" Mean|\n")

    print("Finish     ", end="")
    for time in finish_time:
        print(f"|{time:3}  ", end="")
    print("|-----|\n")

    print("Turnaround |", end="")
    for tat in turn_around_time:
        print(f"{tat:3}  |", end="")
    print(f" {sum(turn_around_time) / process_count:.2f}|\n")

    print("NormTurn   |", end="")
    for nt in norm_turn:
        print(f"{nt:.2f}|", end="")
    print(f" {sum(norm_turn) / process_count:.2f}|\n")
