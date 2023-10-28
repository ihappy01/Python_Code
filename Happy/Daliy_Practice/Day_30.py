# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false

# s="({})"


s = "()[]{}"

def valid_string(s):
  d = {')':'(',']':'[','}':'{'}
  l = []

  for ch in s:
      if ch in d.values():
          l.append(ch)
      elif ch in d.keys():
          if not l or l.pop() != d[ch]:
              return False
      else:
          return False

  return not l

print(valid_string("()"))
print(valid_string("()[]{}"))
print(valid_string("(]"))
