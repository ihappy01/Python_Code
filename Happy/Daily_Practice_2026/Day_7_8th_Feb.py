
class Workload:
    def __init__(self,duration,workload_type):
        self.duration = duration
        self.workload_type = workload_type

    def start(self):
        print(f"dd "
              f"duration ={self.duration} "
              f'workload = {self.workload_type} '
              f'bs=10m'
              )

    def display(self):
        print(f"The {self.workload_type} is running")

class Vdbench(Workload):
    def __init__(self,duration,workload_type,profile):
        super().__init__(duration,workload_type)
        self.profile = profile

    def start(self):
        print(f'dd duration={self.duration} workload={self.workload_type} profile={self.profile} bs=10')


w = Workload(10,'Fio')
w.start()
w.display()

vd = Vdbench(20,'vd1','EDA')
vd.start()
vd.display()

