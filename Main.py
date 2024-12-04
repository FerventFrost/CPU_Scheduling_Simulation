from Gant_Chart import ProcessGanttChart
from Process_Class import ProcessAttributes
from Scheduling_Algorithms import Scheduling

p1 = ProcessAttributes(1, 24, 0, 0, 0, 0)
p2 = ProcessAttributes(2, 3, 0, 0, 0, 0)
p3 = ProcessAttributes(3, 3, 0, 0, 0, 0)
ProcessList = [p1, p2, p3]
print(ProcessList)

SchedulingAlgorithm = Scheduling()
FCFS = SchedulingAlgorithm.FCFS(ProcessList)
SJF_NonPremptive = SchedulingAlgorithm.SJF_NonPremptive(ProcessList)

print(FCFS[1:3])
print(SJF_NonPremptive[1:3])

Gant = ProcessGanttChart()
Gant.Create_GanttChart("FCFS",FCFS[0])
Gant.Create_GanttChart("SJF Non Premptive", SJF_NonPremptive[0])

