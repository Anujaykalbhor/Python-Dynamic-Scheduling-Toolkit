import threading
import time
import random
from algorithm import fcfs_dynamic, round_robin_dynamic
from utils import clear_timeline, print_timeline, print_stats

processes = []
lock = threading.Lock()

def generate_processes(num_processes, max_arrival_time, max_service_time):
    process_intervals = []
    for i in range(num_processes):
        process_name = f"P{i+1}"
        arrival_time = random.randint(0, max_arrival_time)
        service_time = random.randint(1, max_service_time)
        process_intervals.append({'process_name': process_name, 'arrival_time': arrival_time, 'service_time': service_time})
    return process_intervals

def simulate_process_arrival(intervals):
    global processes
    start_time = time.time()
    for interval in intervals:
        arrival_time = interval['arrival_time']
        sleep_time = max(arrival_time - (time.time() - start_time), 0)
        time.sleep(sleep_time)
        lock.acquire()
        processes.append((interval['process_name'], arrival_time, interval['service_time']))
        lock.release()

def get_real_time_processes():
    global processes
    lock.acquire()
    new_processes = processes[:]
    processes.clear()
    lock.release()
    return new_processes

def clear_global_state():
    global processes
    lock.acquire()
    processes.clear()
    lock.release()

def fcfs_simulation(num_processes, max_arrival_time, max_service_time):
    process_intervals = generate_processes(num_processes, max_arrival_time, max_service_time)
    arrival_thread = threading.Thread(target=simulate_process_arrival, args=(process_intervals,))
    arrival_thread.start()

    last_instant = max(arrival['arrival_time'] + arrival['service_time'] for arrival in process_intervals) + 1
    process_count = num_processes
    timeline = clear_timeline(last_instant, process_count)
    finish_time = [0] * process_count
    turn_around_time = [0] * process_count
    norm_turn = [0] * process_count
    all_processes = []
    current_time = 0

    while current_time < last_instant:
        new_processes = get_real_time_processes()
        if new_processes:
            all_processes.extend(new_processes)
            all_processes.sort(key=lambda x: x[1])  # Sort by arrival time

            timeline, finish_time, turn_around_time, norm_turn = fcfs_dynamic(all_processes, timeline, finish_time, turn_around_time, norm_turn, last_instant)
            
            # Print results
            print("Algorithm: FCFS")
            print_stats(all_processes, finish_time, turn_around_time, norm_turn)
            print_timeline(timeline, [p[0] for p in all_processes])

        time.sleep(1)  # Simulate the passage of time
        current_time += 1

    arrival_thread.join()
    clear_global_state()

def round_robin_simulation(num_processes, max_arrival_time, max_service_time, quantum):
    process_intervals = generate_processes(num_processes, max_arrival_time, max_service_time)
    arrival_thread = threading.Thread(target=simulate_process_arrival, args=(process_intervals,))
    arrival_thread.start()

    last_instant = max(arrival['arrival_time'] + arrival['service_time'] for arrival in process_intervals) + 1
    process_count = num_processes
    timeline = clear_timeline(last_instant, process_count)
    finish_time = [0] * process_count
    turn_around_time = [0] * process_count
    norm_turn = [0] * process_count
    all_processes = []
    current_time = 0

    while current_time < last_instant:
        new_processes = get_real_time_processes()
        if new_processes:
            all_processes.extend(new_processes)
            all_processes.sort(key=lambda x: x[1])  # Sort by arrival time

            timeline, finish_time, turn_around_time, norm_turn = round_robin_dynamic(all_processes, quantum, last_instant)
            
            # Print results
            print(f"Algorithm: Round Robin (Quantum={quantum})")
            print_stats(all_processes, finish_time, turn_around_time, norm_turn)
            print_timeline(timeline, [p[0] for p in all_processes])

        time.sleep(1)  # Simulate the passage of time
        current_time += 1

    arrival_thread.join()
    clear_global_state()

def main():
    num_processes = 10
    max_arrival_time = 5
    max_service_time = 10
    quantum = 2

    print("Running FCFS Algorithm\n")
    fcfs_simulation(num_processes, max_arrival_time, max_service_time)

    time.sleep(2)  # Sleep for a short duration to separate outputs

    print("\nRunning Round Robin Algorithm\n")
    round_robin_simulation(num_processes, max_arrival_time, max_service_time, quantum)

if __name__ == "__main__":
    main()
