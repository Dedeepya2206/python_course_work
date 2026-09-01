'''#1. Print Numbers from 1 to N (Using for loop)

n = int(input("Enter the number:"))

for i in range(1,n+1):
    print(i)'''

'''#2. Print Even Numbers from 1 to N (Using for loop)

n = int(input("Enter the Number:"))

for i in range(0,n+1):
    if i%2==0:
        print(i)'''

'''#3. Sum of Numbers from 1 to N (Using for loop)
n = int(input("Enter the Number:"))
sum=0
for i in range(1,n+1):
    sum =sum + i
    print("Sum of numbers from 1 to N",sum)'''


'''#4. Print Odd Numbers from 1 to N (Using for loop)

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    if i % 2!= 0:
        print(i)
'''

'''#5. Find Factorial of a Number (Using for loop)
n=int(input("Enter the number: "))

fact = 1
for i in range(1,n+1):
    fact = fact *i
print("Factorial is:",fact)'''
'''
#6. Print Multiplication Table of N (Using for loop)

n=int(input("Enter the number: "))

for i in range(1,11):
    print(n,'*',i,'=',n*i)
'''

#7. Check Prime Number (Using for loop)

n = int(input("enter the number: "))
c=0

for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("Prime Number")
else:
    print("not a prime number")

'''#8. Sum of Digits of a Number (Using while loop)
n=int(input("Enter the number:"))

sum=0
while n>0:
    digit = n%10
    sum=sum+digit
    n=n//10
    
print("Sum of digits:", sum)
'''
'''#10. Count Numbers Divisible by 3 (Using for loop)
n=int(input("enter the number:"))
count=0
for i in range(1,n+1):
    if i % 3==0:
        count=count+1
print(count)'''

'''#sqares of a number:
n=int(input("Enter the number:"))

for i in range(1,n+1):
    print(i*i)  
'''
