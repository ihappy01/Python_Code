a = [1, 4, 2, 7, 3, 8,5]
target =5
l=len(a)
values=[]

for i in range(l):
    for j in range(i+1,l):
        if a[i]+a[j]==target:
            values.append((a[i],a[j]))



print(values)

