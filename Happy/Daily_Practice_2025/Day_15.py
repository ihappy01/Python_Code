# Create a math class.Initialize 2 attributes as x and y . Define 2 methods- division and multiplication.
# Create object. Call both methods for that object.


class Math:
  def __init__(self,x,y):
      self.x =x
      self.y =y

  def div(self):
      return self.x/self.y

  def mul(self):
      return self.x * self.y



o= Math(7,8)

div_res =o.div()
print(div_res)
mul_res =o.mul()
print(mul_res)



