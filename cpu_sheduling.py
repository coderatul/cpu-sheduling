import prettytable
at_prcs_mapping = {} # arrivaltime : processess mapping
bt_at_mapping = {} # burst time : arrival time mapping

class CpuSheduling():
    def __init__(self, name:list = [], arrival_time:list = [], burst_time:list = [], time_quantum= None) -> None:
        self.process = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.time_quantum = time_quantum
        
        # displaying processess, arival time and burst time in a tabular format
        print(10*"-","given process data",10*"-")
        table = prettytable.PrettyTable()
        table.field_names = ["Process", "Arrival Time", "Burst Time"]
        for i in range(len(self.process)):
            table.add_row([self.process[i], self.arrival_time[i], self.burst_time[i]])
        print(table)
        print()
        
    def fcfs(self):
        """
        first come first serve short term shdeuling
        """
        for i in range(len(self.process)):
            # creating arrival time : process & burst time : arrival time mapping
            at_prcs_mapping.update({self.arrival_time[i]:self.process[i]})
            bt_at_mapping.update({self.arrival_time[i]:self.burst_time[i]})
        
        # sorted arriavl time 
        self.arrival_time.sort()
        
        # burst time in order of process execution 
        bt_ord = []

        print("fcfs order: ",end="")
        for k in self.arrival_time:
            # printing keys(process) of arrival time(from sorted arrival time list(self.arrival_time))
            if k == self.arrival_time[-1]:
                print(f"{at_prcs_mapping.get(k)}",end="")
            else:
                print(f"{at_prcs_mapping.get(k)} -> ",end="")
            
            # appending burts time of process in the order of their execution
            bt_ord.append(bt_at_mapping.get(k))
        print()
            
        # calculating completion time of each process 
        ct = []
        for j in bt_ord:
            if ct:
                temp = ct[-1] + j
            else:
                temp = j
            ct.append(temp)
        
        print()
        print(30*"-","first come first serve shedule",30*"-")
        print()
        
        # list of turn around time for everyprocess
        tat_list = [a-b for a,b in zip(ct,at)]
        
        # average turn around time
        tat = sum(tat_list) / len(tat_list)
        
        # list of waiting time for each process
        wt_list = [a-b for a,b in zip(tat_list,bt)]
        
        # average waiting time
        wt = sum(wt_list) / len(wt_list)
        
        # printing process, arival time, burst time, completion time, turn around time, waiting time
        table = prettytable.PrettyTable()
        table.field_names = ["Process", "Arrival Time", "Burst Time", "Completion Time", "Turn around time", "waiting time"]
        for i in range(len(self.process)):
            table.add_row([at_prcs_mapping.get(i), self.arrival_time[i], self.burst_time[i],ct[i],tat_list[i],wt_list[i]])
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
    prcs = ["P1","P2","P3","P4","P5"] #process
    at = [0,1,2,3,4] # arrival time
    bt = [8,1,3,2,6] # burst time
    shedule = CpuSheduling(prcs,at,bt) 
    shedule.fcfs()
    

    
    


        