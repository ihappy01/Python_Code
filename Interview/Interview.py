# a = "My Interview"
# print('%.6s'%a)

#
# def MyInt(a):
#
#     months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
#
#     yield months[a]
#
#     yield months[a+2]
#
#
# next_month = MyInt(3)
#
# print(next(next_month), next(next_month))


#
# with open("my_note1.txt","r") as f:
# 	print(f.read(10))


from datetime import datetime

print(datetime.now())

current_time = datetime.now()

date_format = current_time.strftime('%H:%M')
print(date_format)