# Fibonnaci series

for i in range(0,7):
    if i==0:
        print(0)
    elif i==1:
        print(1)
    else:
        n1 = n2
        n2 = n1+n2
        print(n1 ,n2)