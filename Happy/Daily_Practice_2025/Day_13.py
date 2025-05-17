

l = [3,2,6,1,4,5,9,8,7]

s=len(l)
j=1
for i in range(s-1):
    for j in range(i+1,s):
        if l[i]+l[j] == 9:
            print(f'sum of {l[i]} and {l[j]} is 9')