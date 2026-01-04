

ip = '10.44.25.032'

# o = ip.replace(".","-")

# print (f"data-{o}")
# print (f"data-{ip.replace(".","-")}")

o = "data"
l= ip.split('.')
l=[]
# for d in ip

for ch in l:
    o = o+'-'+ch

print(o)

