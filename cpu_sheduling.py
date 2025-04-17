import copy
from typing import List, Dict, Tuple, Optional
import prettytable

class CpuSheduling:
    def __init__(self, prcs: List[str] = [], arrival_time: List[float] = [],
                 burst_time: List[float] = [], time_quantum: Optional[float] = None) -> None:
        """
        Initializes the CPU scheduler with process data.

        Args:
            prcs: List of process names (e.g., ["P1", "P2"]).
            arrival_time: List of arrival times for each process.
            burst_time: List of burst times for each process.
            time_quantum: Time quantum for Round Robin (optional, unused in FCFS).

        Raises:
            ValueError: If input lists have mismatched lengths or contain invalid types.
        """
        self.process: List[str] = prcs
        self.arrival_time: List[float] = arrival_time
        self.burst_time: List[float] = burst_time
        self.time_quantum: Optional[float] = time_quantum
        self.at_prcs_mapping: Dict[float, List[Tuple[str, float]]] = {}

        # Validate input lengths
        if len(self.process) != len(self.arrival_time):
            raise ValueError("Number of processes doesn't match number of arrival times")
        if len(self.process) != len(self.burst_time):
            raise ValueError("Number of processes doesn't match number of burst times")

        # Validate input types
        if not all(isinstance(at, (int, float)) for at in self.arrival_time):
            raise ValueError("Arrival times must be integers or floats")
        if not all(isinstance(bt, (int, float)) for bt in self.burst_time):
            raise ValueError("Burst times must be integers or floats")

        # Display input data
        print(10 * "-", "Given Process Data", 10 * "-")
        table = prettytable.PrettyTable()
        table.field_names = ["Process", "Arrival Time", "Burst Time"]
        for i in range(len(self.process)):
            table.add_row([self.process[i], self.arrival_time[i], self.burst_time[i]])
        print(table, "\n")

    def unique_at(self) -> List[float]:
        """
        Returns a sorted list of unique arrival times.

        Returns:
            A list of unique arrival times in ascending order.
        """
        return sorted(set(self.arrival_time))

    def at_mapping(self) -> Dict[float, List[Tuple[str, float]]]:
        """
        Maps arrival times to lists of (process, burst time) tuples.

        Returns:
            A dictionary where keys are arrival times and values are lists of
            (process, burst time) tuples.
        """
        self.at_prcs_mapping.clear()  # Prevent stale data
        for i, at in enumerate(self.arrival_time):
            if at not in self.at_prcs_mapping:
                self.at_prcs_mapping[at] = []
            self.at_prcs_mapping[at].append((self.process[i], self.burst_time[i]))
        return self.at_prcs_mapping
    # eg : {0: [("P1", 2)], 1: [("P2", 2)], 5: [("P3", 3)], 12: [("P4", 4)]}

    def final_data(self, mapping: Dict[float, List[Tuple[str, float]]], key: str = "process") -> List[float | str]:
        """
        Converts a mapping into a flat list of processes or burst times ordered by arrival time.

        Args:
            mapping: Dictionary mapping arrival times to (process, burst time) tuples.
            key: Either "process" (for process names) or "burst" (for burst times).

        Returns:
            A flat list of either process names or burst times in arrival order.
        """
        listed_data = []
        for at in self.unique_at():
            if at in mapping:
                for proc, bt in mapping[at]:
                    listed_data.append(proc if key == "process" else bt)
        return listed_data

    def fcfs(self) -> None:
        """
        Implements First-Come-First-Serve scheduling.

        Computes completion, turnaround, and waiting times, and displays the schedule
        with a process order (including halts) and a detailed table.
        """
        execution_order = self.final_data(self.at_mapping(), "process")
        process_ord = copy.deepcopy(execution_order)
        bt_ord = self.final_data(self.at_mapping(), "burst")

        # Calculate completion times with halts
        ct = []
        current_time = 0
        halt_count = 0
        for i, (proc, bt) in enumerate(zip(execution_order, bt_ord)):
            prcs_at = self.arrival_time[self.process.index(proc)]
            # Check for halt before starting the process
            if prcs_at > current_time:
                halt_duration = prcs_at - current_time
                process_ord.insert(i + halt_count, f"halt for {halt_duration} sec(s)")
                halt_count += 1
                current_time = prcs_at
            # Process execution
            current_time += bt
            ct.append(current_time)

        # Calculate turnaround and waiting times
        at_order = [self.arrival_time[self.process.index(p)] for p in execution_order]
        tat_list = [c - a for c, a in zip(ct, at_order)]
        wt_list = [max(0, t - b) for t, b in zip(tat_list, bt_ord)]
        tat = sum(tat_list) / len(tat_list) if tat_list else 0
        wt = sum(wt_list) / len(wt_list) if wt_list else 0

        # Print process order
        print("fcfs order: ", end="")
        for proc in process_ord:
            print(f"{proc}", end="" if proc == process_ord[-1] else " -> ")
        print("\n")

        # Print table
        table = prettytable.PrettyTable()
        table.field_names = ["Process", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time"]
        for i in range(len(self.process)):
            table.add_row([execution_order[i], at_order[i], bt_ord[i], ct[i], tat_list[i], wt_list[i]])
        print(table)
        print(f"Average turnaround time: {tat:.2f}")
        print(f"Average waiting time: {wt:.2f}")

    def sjf(self):
        """
        shortest job first: non-preemtive
        """
        ...
        
    def srtf(self):
        """
        shortest remaining time first : preemitive
        """
        ...
        
    def rr(self):
        """
        round robbin 
        """
        ...
                     
if __name__ == "__main__":
    prcs = ["P1", "P2", "P3", "P4","P5","P6"]
    at = [4, 19, 2, 3,2, 2]
    bt = [1, 2 ,7 ,1 ,2, 2]
    s1 = CpuSheduling(prcs, at, bt)
    s1.fcfs()