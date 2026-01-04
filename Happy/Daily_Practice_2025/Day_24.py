import subprocess


# subprocess.run('dir',shell=True)
# p1 =subprocess.run('dir',shell=True,stdout=subprocess.PIPE,text=True)
#
# print(p1.args)
# print(p1.returncode)
# print(p1.stdout)

with open("cmd_output.txt",'w') as f:
    p1 = subprocess.run('dir', shell=True, stdout=f, text=True)


# subprocess.run('dir')
# subprocess.run(['cmd', '/c', 'dir'])