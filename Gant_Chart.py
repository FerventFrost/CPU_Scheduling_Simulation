import matplotlib.pyplot as plt
import numpy as np
from Process_Class import ProcessAttributes

class Gant_Chart:
    def __init__(self):
        self._Color = ['skyblue', 'salmon', 'lightgreen']

    def create_dataframe(self,Algorithm_Name:str,Process:list[ProcessAttributes]):
        _Process = Process.copy()
        _Data = []
        _PIDList = []

        for process in _Process:
            _PIDList.append(process.pid)
            _Data.append([process.BurstTime])

        for i in range(len(_Data)):
            plt.barh(["Process"], _Data[i], left=np.sum(_Data[:i]), color=self._Color[i%3], label=f'Process {_PIDList[i]}')

        plt.xlabel('Values')
        plt.title(f"{Algorithm_Name}")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    p1 = ProcessAttributes(1, 24, 0, 0, 0, 0)
    p2 = ProcessAttributes(2, 3, 0, 0, 0, 0)
    p3 = ProcessAttributes(3, 3, 0, 0, 0, 0)
    p4 = ProcessAttributes(3, 3, 0, 0, 0, 0)
    ProcessList = [p1, p2, p3,p4]
    print(ProcessList)
    
    Gant = Gant_Chart(ProcessList)
    # Gant.create_dataframe()
    Gant.create_dataframe()

