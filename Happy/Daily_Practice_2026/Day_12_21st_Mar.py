
class Workload:
    def __init__(self ,duration ,workload_type):
        self.duration = duration
        self.workload_type = workload_type

    def start(self):
        print(f"dd duration={self.duration} workload_type={self.workload_type} bs= 1MB")

    def display(self):
        print(f"Workload {self.workload_type} is running")

class Vdbench(Workload):
    def __init__(self ,duration ,workload_type ,profile):
        super().__init__(duration ,workload_type)
        self.profile = profile

    def start(self):
        print(f"dd duration={self.duration} workload_type={self.workload_type} profile={self.profile} bs= 1MB")


vd1 = Vdbench(10 ,'FIO' ,'EDA')

vd1.start()
vd1.display()