

l = ["abc",5,78,34]

l.append(1)
print(l)

l2 =["a","b"]
l.extend(l2)

print(l)

l.insert(1,"Indrajeet")
print(l)

l.remove('a')
print(l)

ele=l.pop()
print(ele)
print(l)

# l.clear()
# print(l)

index=l.index("Indrajeet",0,5)
print(index)
index=l.index("Indrajeet")
print(index)

l1=[45,2,78,245,88]
value_max=max(l1)
print(value_max)

value_min = n=min(l1)
print(value_min)

l_length =len(l)
print(l_length)

l1.sort()
print(l1)

l2 =[3,56,1,67,2]
l2_sort=sorted(l2)
print(l2_sort)
