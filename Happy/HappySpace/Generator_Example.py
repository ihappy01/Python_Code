"""
Generators in Python are special type of functions that allow you to create an
iterable sequence of values. A generator function returns a generator object,
which can be used to generate the values one-by-one as you iterate over it.
Generators are a powerful tool for working with large or complex data sets,
as they allow you to generate the values on-the-fly,
rather than having to create and store the entire sequence in memory.
"""

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
# l= ["2","Happy","cold",99]
#
# value= iter(l)
#
# print(next(value))
# print(next(value))
# print(next(value))