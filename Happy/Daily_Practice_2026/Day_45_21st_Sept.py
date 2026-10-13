# Open a json file and convert it into a dictionary


with open(r'Files\json_example.json','r') as f:
    # txt=f.read()
#     # print(txt)
    for line in f:
        print(line,end=' ')