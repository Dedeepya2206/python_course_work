'''
file=open('pfs-63.txt','r') # To read the file
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

with open ('pfs-63.txt','r')as file: #To read and set the cursor
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())

with open('mysql.txt','w') as file: #To write a file
    file.write("DDL,DML")

with open ('pfs-63.txt','w') as file: #To override the file
    file.write("Shifted to Branch 1")

with open ('pfs-63.txt','a') as file: #To append
    file.write(". only for today")


with open ('pfs-63.txt','a+') as file: #To write and append
    file.write(", Tom same branch 5")
    file.seek(0)
    print(file.read())
'''
