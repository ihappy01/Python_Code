

# from datetime import datetime
#
# t=datetime.now()
# # print(t)
#
# t_output = t.strftime("%H:%M")
# print(t_output)

def is_possible(l1, l2):
  """
  Returns True if the words in l1 can be formed from the characters in l2.

  Args:
    l1: The list of words.
    l2: The list of characters.

  Returns:
    True if the words in l1 can be formed from the characters in l2.
  """

  # d = {}
  # for c in l2:
  #   if c not in d:
  #     d[c] = 0
  #   d[c] += 1
  #
  # for word in l1:
  #   for c in word:
  #     if c not in d or d[c] == 0:
  #       return False
  #
  #   for c in word:
  #     d[c] -= 1
  #
  # return True


# l1 = ["hello", "world","are"]
# # l2 = ['a','r','e','d']
# l1= ["is","are","then","that"]
# l2= ['a','i','s']
#
# for word in l1:
#     for ch in word:
#       if ch not in l2:
#         print(f"{word} cannot be formed formed from given list")
#         break
#       else:
#         print(f"{word} can be formed formed from given list")
#         break


def reverse_substring(s,size):
  i=0
  result=""
  l=len(s)
  while i<l:
    if i<l:
      result = result+s[i:i+size][::-1]
      i=i+size
    else:
      result=result+s[i:][::-1]
      break
  return result


s= "Hello World"
size=4
rev= reverse_substring(s,size)
print(rev)