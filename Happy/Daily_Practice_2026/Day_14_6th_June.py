
class Workload:
    def __init__(self,wd,duration):
        self.wd =wd
        self.duration = duration

    def command(self):
        cmd = f'dd workload={self.wd} duration={self.duration} bs=1kb'
        print(cmd)

    def display(self):
        print(f"The {self.wd} workload is running")


# w1= Workload('Fio','5min')
# w1.command()
# w1.display()

class Vdbench(Workload):
    def __init__(self,wd,duration,profile):
        super().__init__(wd,duration)
        self.profile = profile
    def command(self):
        cmd = f'dd workload={self.wd} duration={self.duration} profile={self.profile} bs=1kb'
        print(cmd)

v1 = Vdbench('VD','10min','eda')
v1.command()
v1.display()

