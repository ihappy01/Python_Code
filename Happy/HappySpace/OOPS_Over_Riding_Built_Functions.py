"""
-For all built in function there is an magic method defined in Python which we need modify to override it
-Magic function (starting and ending with __ ) are automatically called
-When we don't return from method and only using print in that method then by default 'None' is returned

https://www.google.com/search?q=python+overloading+and+overriding&rlz=1C1CHBF_enIN1129IN1129&oq=python+over&gs_lcrp=EgZjaHJvbWUqBwgBEAAYgAQyBwgAEAAYgAQyBwgBEAAYgAQyBwgCEAAYgAQyBggDEEUYOTIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTE1MTE2ajBqN6gCALACAA&sourceid=chrome&source=chrome.ob&ie=UTF-8

"""

class Cart:
    def __init__(self,basket1,basket2,basket3):
        self.clothes = basket1
        self.electronics = basket2
        self.others = basket3


    def __len__(self):
        return len(self.clothes)+len(self.electronics)+len(self.others)

    def __str__(self):
        return "This is cart class object"

c1 = Cart(["T-shirt","Pant","Kurta"],["Mobile","Laptop"],["Table"])
print(len(c1))