from Happy.HappySpace.test_prime import lower_range

prefix = 'rquota-fs-'
start = 1
end = 50

filesystem = [f'{prefix}{i:02d}' for i in range(start,end+1)]
print(filesystem)

salary = 1250000
print(f'You salary is {salary:,}')

'''
write a program l =[1,0,0,0,1,1,1,0,1,0]  to get all 0's at starting and 1's at last  

'''

l =[1,0,0,0,1,1,1,0,1,0]
lo=[]
li=[]

for i in l:
    if i < 1:
        lo.append(i)
    else:
        li.append(i)

lo.append(li)
print(lo)

# l.sort()
print(l)
lm=sorted(l)
print(lm)
