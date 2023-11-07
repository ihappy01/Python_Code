
# class Cart:
#     def __init__(self,basket1,basket2,basket3):
#         self.clothes = basket1
#         self.electronics = basket2
#         self.others = basket3
#
#
#     def __len__(self):
#         return len(self.clothes)+len(self.electronics)+len(self.others)
#
#
#     def __str__(self):
#         return "The length of the cart is"
#
#
# c1= Cart(['T-shirt','Pants'],['Mobile'],['Chairs'])
#
# print(len(c1))
# print(c1)
# # print(dir(Cart))


text=  "Hello Good Morning, Indrajeet"
# s=''
# for ch in text:
#     s=ch+s
#
# print("The reverse string is :",s)

# s= text.split(' ')
# l=[]
# for words in s:
#     l.append(words[::-1])
#
# rev = " ".join(l)
# print("String after reversing each word is sentence :",rev)



# i=0
# l=len(text)
# s=""
# size=3
#
# while i<l:
#     s=s+text[i:i+size][::-1]
#     i= i+size
#
# print(s)

ch=list(text)
l=len(text)
left,right=0,l-1

while left<right:
    if ch[left]==" ":
        left=left+1
    if ch[right]== " ":
        right=right-1

    ch[left],ch[right]=ch[right],ch[left]

    left=left+1
    right=right-1


print("".join(ch))