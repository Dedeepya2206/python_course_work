'''n=int(input("enter a number: "))
if n>0:
    print("Positive number")
else:
    print("negative number")
'''
'''n=int(input("enter a number: "))
if n%2==0:
    print("Even number")
else:
    print("odd number)
    '''
'''n=int(input("enter a number: "))
if n%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5)
    '''
'''
n=int(input("enter a number: "))
if n%3==0 and n%7==0:
    print("Divisible by both 3 and 7")  
else:
    print("Not divisible by both")
    '''
'''n=int(input("enter a number: "))
if n%400==0 or (n%4==0 and n%100!=0):
    print("Leap Year")  
else:
    print("not a leap year")'''
'''n=int(input("enter a number: "))
if n>35:
    print("Pass")  
else:
    print("fail")
    '''
'''n=int(input("enter a number: "))
l=list(str(n))
if len(l)==3:
    print("3-digit number")  
else:
    print("not a 3-digit number")'''
'''c=input()
if c in "aeiouAEIOU":
    print("Vowel")
else:
    print("not a vowel")'''

'''a=int(input())
b=int(input())
if a>b:
    print(a)
else:
    print(b)'''
'''a=int(input())
b=int(input())
if a<b:
    print(a)
else:
    print(b)'''
'''n=int(input())
if n==0:
    print("Number is zero")
else:
    print("Not a zero")'''
'''n=int(input())
if n%10==0:
    print("Multiple of 10")
else:
    print("Not a Multiple of 10")'''
'''age=int(input())
if age>18:
    print("Eligible to vote")
else:
    print("Not  Eligible to vote")'''
'''n=int(input())
if 1<=n<=100:
    print("In range")
else:
    print("Not In range")'''
'''a=int(input())
b=int(input())
if b*b==a:
    print(f"{a} is square of {b}")
else:
    print("not a square")'''
'''s1=input()
s2=input()
if s1==s2:
    print("Strings are equal")
else:
    print("Strings are  not equal")'''
'''n=int(input())
if n<2:
    print("Not a prime")
else:
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print("Prime number")
    else:
        print("Not prime")'''
'''n=int(input())
if n>0 and n%2==0:
    print("Positive and even number")
else:
    print("not a positive and even number")'''
'''ch=input()
if ch.isupper():
    print("Uppercase letter")
else:
    print("not a uppercase")'''
'''temp=int(input())
if temp>35:
    print("its hot")
else:
    print("cool")
'''
