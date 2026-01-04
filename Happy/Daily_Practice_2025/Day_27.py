import subprocess

# p1=subprocess.run('dir',shell=True,capture_output=True,text=True )
# p1=subprocess.run('dir',shell=True,stdout=subprocess.PIPE,text=True )

# with open('output.txt','w') as f:
#     p1=subprocess.run('dir',shell=True,stdout=f,text=True )

# Wrong Command execution behaviour
# p1=subprocess.run(['dir','sd'],shell=True,capture_output=True,text=True,check=True )
# print(p1)
# print(p1.args)
# print(p1.returncode)
# print(p1.stdout.decode())
# print(p1.stdout)
print(p1.stderr)