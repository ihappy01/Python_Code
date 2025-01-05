from logging import NullHandler

print("Hello, This is new laptop Lenevo Think pad")


def merge_word(word1,word2):
    merge_str=[]
    for i in range(max(len(word1),len(word2))):
        if i<len(word1):
            merge_str.append(word1[i])
        if i<len(word2):
            merge_str.append(word2[i])

    return merge_str


s = merge_word("abcd","1234567")

print("".join(s))
