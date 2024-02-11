# CPU Scheduling Algorithms

This GitHub repository contains Python implementations of various CPU scheduling algorithms. The current implementation includes the First Come First Serve (FCFS) algorithm.

## First Come First Serve (FCFS)

### Introduction
FCFS is a non-preemptive scheduling algorithm that schedules processes based on their arrival time. The process that arrives first is the first to be executed.

### Implementation

The `CpuScheduling` class is used to represent the CPU scheduling algorithms. The FCFS algorithm is implemented in the `fcfs` method.

*current implementation can only handle unique arrival times*

### Usage

To use the FCFS algorithm with a specific set of processes, arrival times, and burst times, create an instance of the `CpuScheduling` class and call the `fcfs` method.

```python
prcs = ["P1", "P2", "P3", "P4", "P5"]  # process
at = [0, 1, 2, 3, 4]  # arrival time
bt = [8, 1, 3, 2, 6]  # burst time
schedule = CpuScheduling(prcs, at, bt)
schedule.fcfs()
```

### Output

The FCFS algorithm will display the order of process execution, completion time, turn around time, and waiting time in a tabular format.

Feel free to explore other CPU scheduling algorithms by extending the `CpuScheduling` class and implementing additional methods for Shortest Job First (SJF), Shortest Remaining Time First (SRTF), and Round Robin (RR) algorithms.

Happy coding!
