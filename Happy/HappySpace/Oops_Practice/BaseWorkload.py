
class BaseWorkload:
    def __init__(self):
        self.duration = None
        self.verbose = None

    def start(self):
        print("Start Function is called")

    def stop(self):
        print ("Stop function is called")

