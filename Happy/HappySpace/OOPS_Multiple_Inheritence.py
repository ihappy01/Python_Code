class Country:
    # Office = "Delhi"
    def __init__(self):
        print("Country Class Constructor called")
        self.Office = "Delhi"

class State:

    def __init__(self):
        super().__init__()
        print("State Class Constructor called")
        self.Office = "Mumbai"

class District(State,Country):
    def __init__(self):
        super().__init__()
        print("District Class Constructor called")
        self.Office = "Pune"


d = District()
print(d.__dict__)