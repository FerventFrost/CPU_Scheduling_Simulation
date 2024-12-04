from dataclasses import dataclass

@dataclass
class ProcessAttributes:
    pid: int
    BurstTime: int
    ArrivalTime: int
    WaitingTime: int
    TurnAroundTime: int
    Milliseconds: int

    def __str__(self):
        return f"ProcessAttributes(pid={self.pid}, BurstTime={self.BurstTime}, ArrivalTime={self.ArrivalTime}, WaitingTime={self.WaitingTime}, TurnAroundTime={self.TurnAroundTime}, Milliseconds={self.Milliseconds})"
    

if __name__ == "__main__":
  p = ProcessAttributes(1, 2, 3, 4, 5, 6)
  print(p)