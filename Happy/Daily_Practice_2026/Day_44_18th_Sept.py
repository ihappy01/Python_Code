# 67 Write a program to open file and store each word in the form of a dictionary using exceptional handling

try:
    with open('file.txt','r') as f:
        # t= f.readline()
        t= f.read()
        print(t.split(' '))
        d={}
        for i,words in enumerate(t.split(' '),start=1):
            d[i]=words

        print(d)
except Exception as e:
    # exception as e
    print(e)
    print("Exception is raised")
    print(f"Exception is raised {e}")


