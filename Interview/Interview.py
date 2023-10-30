

def greeting(fx):
    def mfx():
        print("Performing addition")
        fx()
    return mfx


@greeting
def add():
    print(7+8)

add()

#
import re

def find_match(func)
    def mfunc():
        with open("file.txt", r) as f:
            text = f.read()
            match = re.findall(r'()',text)
            print(match)
            func()
    return mfunc

@find_match
def file_operation():
    print("The file contains below number of () in it")

file_operation()




# input : "i am python"
# output = "n oh typmai"

# text = "i am python"
# s = ('').join(text)
# print(s)

# rev = text[::-1]
# l= []
# for ch in rev:
#     if ch !=" ":
#         l.append(ch)
#
# print(l)
#
# rev_1=""
#
# for ch in text:
#     for char in l
#         if ch==" ":
#             s=ch+" "
#         else:
#             s=s+ch




#
# rev_1=rev.split()
# print(rev_1)

# space_txt=''

# for ch in text:
#     if ch==" ":


def reverse_string_with_spaces(input_str):
    # Split the input string by spaces
    words = input_str.split()

    # Reverse each word and join them back with spaces
    reversed_words = [word[::-1] for word in words]
    reversed_str = " ".join(reversed_words)

    return reversed_str

# Example usage:
input_str = "i am python"
output_str = reverse_string_with_spaces(input_str)
print(output_str)
