#int float string list tuple dict set bool
#int float str tuple bool will not be affected by changes inside functions
#list tuple dict set will be affected by changes inside functions
#pass by value : when we pass an immutable data type to a function, the function creates a copy of the value and any changes made to the value inside the function do not affect the original value.
'''
def display(n):
    n+=10
    print('Inside:',n)
n=20
display(n)
print('Outside:',n)

def display(n):
    n+=" lang"
    print('Inside:',n)
n="Python"
display(n)
print('Outside:',n)


def display(n):
    n+=10.5
    print('Inside:',n)
n=10.9
display(n)
print('Outside:',n)


def display(n):
    n="True"
    print('Inside:',n)
n="False"
display(n)
print('Outside:',n)


def display(n):
    n=(1,2,3)
    print('Inside:',n)
n=(4,5,6)
display(n)
print('Outside:',n)


def display(n):
    n=[1,2,3]
    print('Inside:',n)
n=[4,5,6,3]
display(n)
print('Outside:',n)

'''