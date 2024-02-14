import copy
import prettytable
at_prcs_mapping = {} # arrivaltime : [processess]
bt_at_mapping = {} # burst time : [processess]

class CpuSheduling():
    def __init__(self, name:list = [], arrival_time:list = [], burst_time:list = [], time_quantum= None) -> None:
        self.process = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.time_quantum = time_quantum
        
        # checking if every process has a arrival time and burst time
        if len(self.process) != len(self.arrival_time):
            raise ValueError("Number of process(s) don't match number of arrival time(s) or vice versa")
        if len(self.process) != len(self.burst_time):
            raise ValueError("Number of process(s) don't match number of burst time(s) or vice versa")
        
        # checking if arrival time and burst time are of integer or float type
        if not all(isinstance(at, (int, float)) for at in self.arrival_time):
            raise ValueError("arrival time can only have integer/float value(s)")
        if not all(isinstance(bt, (int, float)) for bt in self.burst_time):
            raise ValueError("burst time can only have integer/float value(s)")

        # displaying processess, arival time and burst time in a tabular format
        print(10*"-","given process data",10*"-")
        table = prettytable.PrettyTable()
        table.field_names = ["Process", "Arrival Time", "Burst Time"]
        for i in range(len(self.process)):
            table.add_row([self.process[i], self.arrival_time[i], self.burst_time[i]])
        print(table)
        print()
        
    
    def unique_at(self)->list:
        """ returns unique arrival time in ascending order"""
        unique_at = []
        for at in self.arrival_time:
            if at not in unique_at:
                unique_at.append(at)
        unique_at.sort()
        return unique_at
    
    def at_mapping(self)-> dict:
        """ returns mapping of arrival time and processess as a dictionary"""
        for index, at in enumerate(self.arrival_time):
            if at not in at_prcs_mapping:
                at_prcs_mapping[at] = [self.process[index]]
            else:
                at_prcs_mapping[at].append(self.process[index])
        return at_prcs_mapping
    
    def bt_mapping(self)->dict:
        """ returns mapping of burst time and arrival time as a dictionary"""
        for index, at in enumerate(self.arrival_time):
            if at not in bt_at_mapping:
                bt_at_mapping[at] = [self.burst_time[index]]
            else:
                bt_at_mapping[at].append(self.burst_time[index])
        return bt_at_mapping
    
    def final_data(self,mapping:dict)->list:
        """ returns a list of processess in the order of their arrival time or burst time"""
        listed_data = []
        for prcs in self.unique_at():
            listed_data.append(mapping[prcs])
        data = [process for sublist in listed_data for process in sublist]
        return data
    
    def check_halt(self,arrival_time:list, ct:list)->list:
        """ returns index and value if any halt is present in the process order"""
        correction_index = 0
        correction_value = 0

        for at in range(len(ct)-1):
            if arrival_time[at+1] > ct[at]:
                correction_value = arrival_time[at+1] - ct[at]
                correction_index = at+1            
        return [correction_value, correction_index]
            
    def fcfs(self):
        """
        first come first serve short term shdeuling
        """
        execution_order = self.final_data(self.at_mapping()) # process order
        process_ord = copy.deepcopy(execution_order) # process order for printing if correction is required
        bt_ord = self.final_data(self.bt_mapping()) # burst time in the order of arrival time
        
        # calculating completion time of each process 
        ct = []
        for j in bt_ord:
            if ct:
                temp = ct[-1] + j
            else:
                temp = j
            ct.append(temp)    
        
        at = sorted(self.arrival_time) # sorted arrival time
        crrction_val, crrction_index = self.check_halt(at, ct) # correction value and index
        
        # inserting halt for correction
        if crrction_val == 0:
            pass
        else:
            process_ord.insert(crrction_index,f"halt for {crrction_val} sec(s)")

        for correction in ct[crrction_index:]:
            ct[crrction_index] += crrction_val
            crrction_index += 1
            
        # printing process order
        print("fcfs order: ",end="")
        for process in process_ord:
            if process == process_ord[-1]:
                print(f"{process}",end="")
            else:
                print(f"{process} -> ",end="")
        print();print()

        # list of turn around time for everyprocess
        tat_list = [a-b for a,b in zip(ct,sorted(self.arrival_time))]
        
        # average turn around time
        tat = sum(tat_list) / len(tat_list)
        
        # list of waiting time for each process
        wt_list = [a-b for a,b in zip(tat_list,bt_ord)]
        
        # average waiting time
        wt = sum(wt_list) / len(wt_list)
        
        # printing process, arival time, burst time, completion time, turn around time, waiting time
        table = prettytable.PrettyTable()
        table.field_names = ["Process", "Arrival Time", "Burst Time", "Completion Time", "Turn around time", "waiting time"]
        for i in range(len(self.process)):
            table.add_row([execution_order[i], at[i], bt_ord[i],ct[i],tat_list[i],wt_list[i]])
        print(table)
        print(f"turn around time -> {tat}")
        print(f"average waiting time was -> {wt}")
        
        
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
    prcs =["P1","P2","P3","P4"] #process
    at = [0,1,5,12] # arrival time
    bt = [2,2,3,4] # burst time
    shedule = CpuSheduling(prcs,at,bt) 
    shedule.fcfs()
 
        