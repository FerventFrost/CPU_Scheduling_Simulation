from Process_Class import ProcessAttributes
class Scheduling:
  def __init__(self, processes:list[ProcessAttributes]):
    self.processes = processes
  
  def FCFS(self) -> tuple[int, int]:
    _ProcessList = self.processes.copy()
    _AverageWaitingTime = 0
    _AverageTurnAroundTime = 0
    _Len = len(_ProcessList)

    # Dummy Process to finish the last process
    _DummPorcess = ProcessAttributes(0, 0, 0, 0, 0, 0)
    _ProcessList.append(_DummPorcess)

    for i in range(len(_ProcessList) -  1):
      # Calculate Waiting Time for next process
      _ProcessList[i+1].WaitingTime = _ProcessList[i].BurstTime + _ProcessList[i].WaitingTime 
      
      _AverageWaitingTime += _ProcessList[i-1].WaitingTime
      _AverageTurnAroundTime += _ProcessList[i].BurstTime + _ProcessList[i].WaitingTime
      
    _AverageWaitingTime = _AverageWaitingTime / _Len
    _AverageTurnAroundTime = _AverageTurnAroundTime / _Len
    return (_AverageWaitingTime, _AverageTurnAroundTime)


  def SJF_NonPremptive(self):
    pass

  def SJF_Premptive(self):
    pass

  def Priority_NonPremptive(self):
    pass

  def Priority_Premptive(self):
    pass

  def RR(self):
    pass


if __name__ == "__main__":
  p1 = ProcessAttributes(1, 24, 0, 0, 0, 0)
  p2 = ProcessAttributes(2, 3, 0, 0, 0, 0)
  p3 = ProcessAttributes(3, 3, 0, 0, 0, 0)
  ProcessList = [p1, p2, p3]
  print(ProcessList)

  SchedulingAlgorithm = Scheduling(ProcessList)
  print(SchedulingAlgorithm.FCFS())
