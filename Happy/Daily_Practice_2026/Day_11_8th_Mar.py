
class Workload:
    def __init__(self,duration,workload_type):
        self.duration = duration
        self.workload_type = workload_type


    def start(self):
        cmd = f"dd duration={self.duration} workload={self.workload_type}"
        print(cmd)

    def display(self):
        print(f"The workload {self.workload_type} is running")


class VDBench(Workload):
    def __init__(self,duration,workload_type,profile):
        super().__init__(duration,workload_type)
        self.profile =profile

    def start(self):
        print(f"dd duration={self.duration} workload={self.workload_type} profile={self.profile}")


wd= Workload(5,"FIO")
wd.start()
wd.display()
vd =VDBench(10,"VD","EDA")
vd.start()
vd.display()
