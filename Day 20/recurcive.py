'''
def func(argument):
    base case:
       return
    print(argument)
    func(updated value)
func(parameter)


# To print 1 to 10 using recursion
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)

#To print 10 to 1 using recursion
def display(n):
    if n<1:
        return
    print(n)
    display(n-1)
display(10)
 
# To print 10 to 1 using recursion without using print statement before recursive call
def display(n):
    if n>10:
        return
    
    display(n+1)
    print(n)
display(1)

#To print sum of numbers from 1 to n using recursion
def displaysum(n):
    if n==0:
        return 0
    
    return n+ displaysum(n-1)
print(displaysum(8))

# To print product of numbers from 1 to n using recursion
def displayproduct(n):
    if n==1:
        return 1
    return n*displayproduct(n-1)
print(displayproduct(5))


#To print itarate the string using resursion
def displaystring(S):
    if len(S)==0:
        return
    print(S[0])
    displaystring(S[1:])
displaystring("Hello")


# print length of string using recursion by using indexing.
def display(ind):
    if ind==len(s):
        return
    print(s[ind])
    display(ind+1)
s="Python Programming"
display(0)

def display(ind):
    if ind==len(s):
        return
    
    display(ind+1)
    print(s[ind],end='')#to print in reverse order and without line break.
s="Python Programming"
display(0)

#To print each line need to add a new character at the end of each line in the string.

def display(n):
    if n>len(s):
        return
    print(s[:n])
    display(n+1)
s="Python Programming"
display(1)

#To print the length  of characters that based on the length given by the user using recursion method.
def recursive_length(s):
    if s == "":
        return 0
    else:
        return 1 + recursive_length(s[1:])
user_input = input("Enter a string: ")
length = recursive_length(user_input)
print("Length of the string is:", length)

# To print characters based on the width.
def display(ind,w):
    if ind>len(s)-w:
        return
    print(s[ind:ind+w])
    display(ind+1,w)
s="Python Programming"
display(0,10)

#using recursion display the digits using recursions.
def digit(n):
    if n==0:
        return
    else:
        digit(n//10)
        print(n%10)
num=int(input( ))
print("digits are :",end= ' ')
digit(num)

#using recursion display the sum of digits using recursions.
def display(n):
    if n==0:
        return 0
    return n%10+display(n//10)
    
n=987654
print(display(n))
'''


