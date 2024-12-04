from Gant_Chart import Gant_Chart
from Process_Class import ProcessAttributes
from Scheduling_Algorithms import Scheduling

p1 = ProcessAttributes(1, 24, 0, 0, 0, 0)
p2 = ProcessAttributes(2, 3, 0, 0, 0, 0)
p3 = ProcessAttributes(3, 3, 0, 0, 0, 0)
ProcessList = [p1, p2, p3]
print(ProcessList)

SchedulingAlgorithm = Scheduling(ProcessList)
print(SchedulingAlgorithm.FCFS())

Gant = Gant_Chart(ProcessList)
Gant.create_dataframe()


