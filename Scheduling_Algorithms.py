from Process_Class import ProcessAttributes
class Scheduling:
  def __init__(self):
    pass
  
  def FCFS(self, Process:list[ProcessAttributes]) -> tuple[list[ProcessAttributes],int, int]:
    _ProcessList = Process.copy()
    _AverageWaitingTime = 0
    _AverageTurnAroundTime = _ProcessList[0].BurstTime
    _Len = len(_ProcessList)

    _ProcessList[0].WaitingTime = 0
    _ProcessList[0].TurnAroundTime = _ProcessList[0].BurstTime
    for i in range(1, _Len):
      _ProcessList[i].TurnAroundTime = _ProcessList[i].BurstTime + _ProcessList[i - 1].TurnAroundTime

      _AverageTurnAroundTime += _ProcessList[i].TurnAroundTime
      _AverageWaitingTime += _ProcessList[i - 1].TurnAroundTime

    _AverageWaitingTime = _AverageWaitingTime / _Len
    _AverageTurnAroundTime = _AverageTurnAroundTime / _Len
    return (_ProcessList, _AverageWaitingTime, _AverageTurnAroundTime)


  def SJF_NonPremptive(self, Process:list[ProcessAttributes])-> tuple[list[ProcessAttributes],int, int]:
    _ProcessList = Process.copy()
    _ProcessList.sort(key=lambda x: x.BurstTime)

    return self.FCFS(_ProcessList)

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

  SchedulingAlgorithm = Scheduling()
  print(SchedulingAlgorithm.FCFS(ProcessList))
