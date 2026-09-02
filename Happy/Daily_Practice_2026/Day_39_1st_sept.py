import textwrap

from pythonProject.Pytest.test_logging import filehandler

s = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability."

# r = textwrap.fill(s,5)
# print(r)
# print(textwrap.fill(s,5))
#
# print(textwrap.wrap(s))

l = [44,25,14,76,25,85,84,23,87,4,32,90,9,99,105,101]

m = l[0]
sm = 0
for i in l:
    if i > m:

        sm = m
        m=i
    elif i> sm and i != m:
        sm =i


print(m)
print(sm)

