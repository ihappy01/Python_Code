# s="Hello WOrld"
# r=""
#
# for ch in s:
#     r=ch+r
#
# print(r)
import json

l= [2,4,5,7]

# l.insert(2,88)
# l.append(99)
# print(l)
#
# l.remove(4)
# l.pop(0)
# # print(l)
# l1=[1,2,3,4]
# l.extend(l1)
# # print(l)
#
d={"a":1,"b":2}
d1={'c':3,'d':4}
data = json.dumps(d,indent=4)
print(d)
# d.update(d)
# print(d)
#
# d.pop('b')
#
# print(d)

# for i in range(1,20):
#     if i==1:
#         continue
#     else:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)


def greeting(fx):
    def mfx():
        print("Before funtion call")
        fx()

    return mfx

@greeting
def add():
    print(8+8)

add()