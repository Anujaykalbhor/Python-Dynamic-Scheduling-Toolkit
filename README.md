# Python-Dynamic-Scheduling-Toolkit
# CPU Scheduling Algorithms

## Overview

This project demonstrates the implementation and comparison of various CPU scheduling algorithms, including First-Come, First-Served (FCFS) and Round Robin (RR). These algorithms are essential for process management in operating systems, ensuring efficient execution of processes and resource utilization.

## Features

- Dynamic process generation and simulation.
- Implementation of FCFS and Round Robin scheduling algorithms.
- Real-time process arrival simulation.
- Detailed statistics and visualization of scheduling timelines.

## Algorithms Implemented

1. **First-Come, First-Served (FCFS):**
   - Processes are executed in the order they arrive.
   - Simple and easy to implement.
   - May cause the "convoy effect" where short processes wait for long processes to complete.

2. **Round Robin (RR):**
   - Each process is assigned a fixed time slot (quantum).
   - Processes are executed in a cyclic order.
   - Provides better response time for short processes.

## Project Structure

- `main.py`: Main script to run the simulation.
- `parser.py`: Handles process generation and simulation.
- `algorithm.py`: Contains the implementation of FCFS and Round Robin algorithms.
- `utils.py`: Utility functions for clearing timelines and printing results.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Anujaykalbhor/Python-Dynamic-Scheduling-Toolkit.git
   cd cpu-scheduling-algorithms
   
2. Ensure you have Python installed (version 3.6 or above).


## The simulation will execute both the FCFS and Round Robin algorithms and print the results, including detailed statistics and timeline visualizations.
