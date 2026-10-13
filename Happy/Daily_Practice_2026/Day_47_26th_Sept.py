

with open('Files/text_file.txt','r') as f:
    # data= f.read()
    # print(data)
    # d=(f.readlines())
    # print(d[8])
    dd = f.read().splitlines()
    print(dd)

with open('Files/text_write_file.txt','a') as f:
    f.write("This is line in written through python program")


with open('Files/text_write_file.txt','w') as f:
    f.write("This line will overwrite existing file")


# import os
# if os.path.exists('Files/text_write_file.txt'):
#     os.remove('Files/text_write_file.txt')
# else:
#     print("File does not exit")
