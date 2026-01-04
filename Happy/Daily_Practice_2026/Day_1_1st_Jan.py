
class TestSolarisNfsv4Support:
    def __init__(self,ip,workload):
        self.ip = ip
        self.workload =workload


    def run_workload_on_solaris_initiator(self):
        self.duration = 100
        print(f"The ip of the system id {self.ip}")
        print(f"The work load running in is {self.workload}")

    def check_workload_duration(self):
        print(f"The duration of the workload is {self.duration}")

    def modify_workload_duration(self):
        self.duration= self.duration +10





test1 = TestSolarisNfsv4Support("10.132.14.34","DT")

test1.run_workload_on_solaris_initiator()
test1.check_workload_duration()
test1.modify_workload_duration()
test1.check_workload_duration()
