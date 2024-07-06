import threading
import time
import random

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
