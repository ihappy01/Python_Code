
def num():
    for i in range(10):
        yield i


gen_ob=num()
# print(next(gen_ob))
# print(next(gen_ob))
# print(next(gen_ob))
# print(next(gen_ob))

for i in gen_ob:
    print(i)

# second for loop does not print anything as in generator we can use the value only once
for i in gen_ob:
    print(i)

# ---------------Iterator -----------------------------
print("---------------Iterator------------------")
l= ["2","Happy","cold",99]

value= iter(l)

print(next(value))
print(next(value))
print(next(value))