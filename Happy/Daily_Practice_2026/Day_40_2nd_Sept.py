l = [9,55,87,24,91,56,83,19,78,85,88,99]

m = 0
sm = 0
tm =0

for i in l:
    if i> m:
        tm = sm
        sm = m
        m = i
    if i > sm and i != m:
        tm = sm
        sm = i
    if i> tm and i < sm:
        tm = i


print(m)
print(sm)
print(tm)


