

# text="Hello World"
#
# d={}
#
# for ch in text:
#     d[ch]=d.get(ch,0)+1
#
#
# print(d)
# print(max(d,key=d.get))

# ----------------------

# def version_check(v1,v2):
#     value_v1= list(map(int,v1.split('.')))
#     value_v2= list(map(int,v2.split('.')))
#
#     for i in range(3):
#         if v1[i]>v2[i]:
#             return v1
#         elif v1[i]<v2[i]:
#             return  v2
#
#
#     return "Version is same"
#
# version_1 = "1.26.5"
# version_2 = "1.24.2"
#
# check=version_check(version_1,version_2)
#
# print(check)
# ================
def compare_versions(ver1, ver2):
    # Split the version strings into components
    ver1_components = list(map(int, ver1.split('.')))
    ver2_components = list(map(int, ver2.split('.')))

    # Compare the major, minor, and patch components
    for i in range(3):
        if ver1_components[i] < ver2_components[i]:
            return ver2
        elif ver1_components[i] > ver2_components[i]:
            return ver1

    # If all components are equal, the versions are the same
    return "Versions are the same"

# Version strings
ver_1 = "1.23.4"
ver_2 = "1.3.4"

# Compare the versions
latest_version = compare_versions(ver_1, ver_2)

if latest_version == "Versions are the same":
    print("Both versions are the same.")
else:
    print(f"The latest version is {latest_version}")
# ----------------------------------------


class A:
    def method1(self):
        print("A")


class B(A):
    def method1(self):
        print("B")

class C:
    pass

ob= A()
ob1 =B()
# A a = new B()
A = B()

ob.method1()  # A
ob1.method1()  # B

A.method1()  # B

# --------------------