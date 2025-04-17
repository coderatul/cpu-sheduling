# CPU Scheduling Algorithms
---
This repository provides Python implementations of CPU scheduling algorithms, starting with **First Come First Serve (FCFS)**.

<img src="https://github.com/user-attachments/assets/c3b08ea9-09cc-480f-a0e6-9fd7a8673b11" width="350" height="200">



## First Come First Serve (FCFS)

- **Overview**: A non-preemptive algorithm executing processes in arrival order.
- **Features**: Handles duplicate arrival times and detects halts effectively.

### Usage

```python
prcs = ["P1", "P2", "P3", "P4", "P5", "P6"]
at = [4, 19, 2, 3, 2, 2]
bt = [1, 2, 7, 1, 2, 2]
s1 = CpuSheduling(prcs, at, bt)
s1.fcfs()
```

### Output
- Displays execution order, completion time, turnaround time, and waiting time in a tabular format.
<img src="https://github.com/user-attachments/assets/9a88b96d-15e2-4ae0-875e-c7375befb5e6" width="660" height="237">

## Future Development
> Planned implementations include **SJF**, **SRTF**, and **RR** algorithms.

## Contributions
We welcome contributions! Help implement SJF, SRTF, or RR by forking the repo, adding your code, and submitting a pull request. Let’s build this together!

*last Release was on : April 17, 2025*
