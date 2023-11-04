
# from datetime import datetime
#
# ob=datetime.now()
# print(ob.strftime("%d/%m/%y %H:%M%S"))

class FiveDivisionError(Exception):
    def __init__(self):
        print("Division by 5 is not allowed for this functionality")

try:
    a=6
    b=0
    if b==5:
        raise FiveDivisionError
    div=a/b
    print(div)

except (FiveDivisionError,Exception) as e:
    print(e)

