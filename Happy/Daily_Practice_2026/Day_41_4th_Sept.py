l = [9,55,87,24,91,56,101,83,19,78,85,88,99]

for i in range(len(l)):
    for j in range(len(l)-1):
        if l[i] < l [j]:
            l[i],l[j] = l[j],l[i]


print(l)
