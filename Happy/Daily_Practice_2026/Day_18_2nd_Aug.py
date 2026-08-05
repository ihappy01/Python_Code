
# ip = '10.46.23.112'
#
# output = f'data-{ip.replace('.','-')}'
# print(output)


class Workload():
    def __init__(self,workload_type,duration):
        self.duration = duration
        self.workload_type = workload_type

    def start(self):
        print(f"dd workload={self.workload_type} duration={self.duration} bs=1m")

    def display(self):
        print(f"The workload {self.workload_type} is running")

wd1 = Workload('Fio','600')
wd1.start()
wd1.display()

class Vdbench(Workload):
    def __init__(self,workload_type,duration,EDA):
        super().__init__(workload_type,duration)
        self.EDA = EDA

    def start(self):
        print(f"dd workload={self.workload_type} duration={self.duration} EDA={self.EDA} bs=1m")


wd2 = Vdbench('vdbench1',900,'profile1')
wd2.start()
wd2.display()