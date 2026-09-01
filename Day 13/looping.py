# for --->to iterate in a sequence  ,we know how many steps to itearte is for loop,updation is automatic
#sequnece--->we have lsit,tuple ,string we can do iterations
#range ---->to genarte numerical value

#1.when ever you need indexes you nedd to keep the range(len(l)) ,otherwise you can give for i in s:
'''s="python Programming"
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])'''


'''l=[23,45,12,34,50,24,35,68,75,34,10]

for i in l:
    print(i,end="")'''

#iterate a list using len function#even indexes sum
'''l=[23,45,12,34,50,24,35,68,75,34,10]

sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+i
        print(i,l[i])
print(sum)
'''
#set,dict you can t use rage function
#list,tuple range function is used


#FACTORIAL OF  A NUMEBR PROGRAMM
'''
factorial of a number
5 -->1*2*3*4*5=125

'''
'''
step-1 n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(i)'''
'''
step-2
fact = 1
fact=fact * i--->fact*=i
use the f string
factorial of {n} is {fact}

'''
'''
n= int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact *= i

print(f" Factorial of {n} is {fact}")
'''



#HWO TO TAKE INPUT FROM THE USER
#HWO TO TAKE THE NAME
#HOW TO TAKE MARKS
#HOW TO TAKE A DICT
#HOW TO ASSIGN VLAUS TO IT
#HIGHEST AND LOWEST MARKS
#MAXIMUM MARK =0

#input as dict
'''data={}
n=int(input("Enter the no of studnets: "))
max_marks=0
for i in range(n):
    name=input("Enter the name: ")
    marks=int(input("Enter the marks: "))
    if marks > max_marks:
        max_marks = marks
    data[name]=marks
print(data)
print("Maximum Marks: ",max_marks)'''


#enter the product
#prodcut
#price
#qunatity
#bill 15*3 


n=int(input("Enter the no of products: "))
total_bill=0
products={}
for i in range(n):
    product = input(f"product - {i}:")
    price= float(input(f" price -{i}: "))
    quantity = int(input(f"quantity-{i}: "))

    final_price = price * quantity

    total_bill += final_price

    products[product]=f'{price}*{quantity}={final_price}'

print(products)
print("Total Bill:",total_bill)
