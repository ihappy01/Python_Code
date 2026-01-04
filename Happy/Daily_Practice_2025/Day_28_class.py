

class Workload():
    def __init__(self,duration,workload_type):
        self.duration = duration
        self.workload_type = workload_type
        self.command=""

    def update_command(self):
        self.command = f"dd if=/tmp/fs_1 of=tmp/log_fs_1 duration={self.duration} workload_type={self.workload_type}"


    def display(self):
        self.update_command()
        print(f"The command is \n {self.command}")


class DT(Workload):
    def __init__(self,duration,workload_type,iops):
        super().__init__(duration,workload_type)
        self.iops = iops
        
    def update_command(self):
        self.command = f"dd if=/tmp/fs_1 of=tmp/log_fs_1 duration={self.duration} workload_type={self.workload_type} iops={self.iops}"


w1=Workload(300,'Fio')

w1.display()

w2= DT(350,'DT',5000)
w2.display()

