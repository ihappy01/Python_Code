
prefix ='rquota-fs-'
start = 1
end = 50

filesystem_list = [f'{prefix}{i:02d}'for i in range(start,end)]
print(filesystem_list)