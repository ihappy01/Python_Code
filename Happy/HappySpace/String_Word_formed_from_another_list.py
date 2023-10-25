# Partially working
l1= ["is","are","then","that"]
l2= ['t','a','i','s','e','r']


for word in l1:
    for ch in word:
        if ch not in l2:
            print(f"{word} cannot be from the given list")
            break
else:
     print(f"{word} can be from the given list")
