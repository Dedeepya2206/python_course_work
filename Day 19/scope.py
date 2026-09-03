'''
#local and global variables
#x=10 is a global vaiable because it is defined outside the function.
def display(n):
    n+=10
    print('Inside:',n)
n=10
display(n)
print('outside:',n)

#we can acess the global variable inside the function because it is defined outside the function.
def display():
    print('Inside:',n)

n=10
display()
print('outside:',n)

#we can not access the local variable outside the function because it is defined inside the function.
def display():
    n=10
    print ('Inside:',n)

display()
print('outside:',n)

#we can access the global variable inside the function because it is defined outside
def display():
    global n
    n=10
    print('Inside:',n)
display()
print('outside:',n)

#we can not update the value of the global variable inside the fn because it is defined outside the fn.
def display(n):
    n='PFS'
    print("Upadted Course :",n)
n='JFS'
display(n)
print("Final Course :",n)

#using global keyword we can update the value of the global variable inside the function.

def display():
    global n
    n='PFS'
    print("Updated Course :",n)
n='JFS'
display()
print('Final Course :',n)

 #nonlocal variables
 #nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.
n='JFS'
    def update():
        nonlocal n
        n='PFS'
        print("Updated Course:",n)
    update()
    print("Final Course:",n)

display()
'''

l=[1,2,3,4,5]
max=20
sum=10
print(sum(l))#get an error because sum is a bulit-in function in python and we have assigned a value to it.so it is not able to perform the sum operation on the list l. To avoid this error we can use bulit-in fn sum() by using the builtins module. 