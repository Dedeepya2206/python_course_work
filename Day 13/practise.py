'''#1. Positive or Negative
n = int(input("Enter the number: "))
if n>0:
    print("Positive number")
else:
    print("Negative number")'''

'''
#2.Even or Odd
n = int(input("Enter the number: "))

if n%2==0:
    print("Even number")
else:
    print("Odd number")'''


'''#3.Divisible by 5
n = int(input("Enter the number: "))

if n%5==0:
    print("Divisible by 5")'''


'''#4.Divisible by 3 and 7
n= int(input("Enter the number: "))

if n%3==0 and n%7==0:
    print("Divisible by both 3 and 7")
else:
    print("not divisbile by 3 and 7")'''

'''5.#check for Leap Year
n = int(input("Enter the number: "))

if n%4==0:
    print("Leap year")'''

'''#6.check Pass or Fail(passing marks = 35)
n = int(input("Enter the number: "))

if n>=35:
    print("Pass")
'''

'''#7. Check if number is 3-digit
n = int(input("Enter the number: "))

if n>=100 and n<=999:
    print("3-digit number")'''

'''#8. Check if character is vowel
n = input("Enter the charachter: ")

if n in 'aeiouAEIOU':
    print("vowel")

'''
'''#9. Check greatest of two numbers
n1 = int(input("Enter the number1:  "))
n2 = int(input("Enter the number2: "))

if n1>n2:
    print(f"{n1} is greatest number")
elif n2>n1:
    print(f"{n2} is greatest number ")
else:
    print(f"both numbers are greatest")'''

'''#10. Check smallest of two numbers
n1 = int(input("Enter the number1:  "))
n2 = int(input("Enter the number2: "))

if n1<n2:
    print(f"{n1} is smallest number")
elif n2<n1:
    print(f"{n2} is smallest number ")
else:
    print(f"both numbers are smallest")
'''

'''#11. Check if number is zero
n = int(input("Enter the number1:  "))

if n==0:
    print("Number is zero")'''

'''#12. Check if number is multiple of 10

n = int(input("Enter the number: "))

if n%10==0:
    print("multiple of 10")'''


'''#13. Check if age is eligible to vote (18+)

n = int(input("Enter the number: "))

if n>=18:
    print("eligible to vote ")
'''

'''#14. Check if number is between 1 and 100

n = int(input("Enter the number: "))

if 1<=n<=100:
    print("in range")'''

'''#15. Check if number is square of another
n= int(input("Enter the number:"))
m= math.sqrt()
'''

'''#16. Check if two strings are equal

n= input("Enter the number:")
m= input("Enter the number:")

if n==m:
    print("Strings are equal")'''


'''#18. Check if number is positive and even
n = int(input("Enter the number: "))

if n>0 and n%2==0:
    print("Positive and even number")'''
'''
#19. Check if character is uppercase
n = input("Enter the charchter: ")

if n.isupper():
    print(f"{n} is uppercase letter")'''

'''#20. Check if temperature is hot (>30°C)
n = int(input("Enter the number: "))

if n>=30:
    print("It's hot")

'''


'''#1. Check if a number is a 4-digit even number

n = int(input("Enter the number: "))

if 1000>=n>=9999 and n%2==0:
    print("4-digit even number")
'''


'''
#2.Check if a character is a consonant

n= input("enter the charcter: ")

if len(n)==1 and n.isalpha():
    if n.lower() not in "aeiou":
        print("Consonant")
    else:
        print("Vowel")
else:
    print("Invalid input")
'''



'''#3. Check if a number is divisible by 2 or 3 but not both 
n= int(input("Enter the number: "))

if n%2==0 and n%3==0:
    print("Divisible by both 2 and 3 ")

else:
    print("Divisible by 2 only")
'''


'''#4. Check if a number is negative and odd

n = int(input("Enter the number: "))

if n<0:
    print("Negative")
else:
    print("Odd number")'''

'''#5. Check if a string starts with a vowel
n=input("enter the value: ")

if n[0] in "aeiouAEIOU":
    print("starts with vowel")
'''

'''#6. Check if three sides form a valid triangle

a=int(input("Enter the  side A: "))
b=int(input("Enter the side B: "))
c=int(input("Enter the Side C: "))

if a+b>c and a+c>b and b+c>a:
    print("valid triangle")
else:
    print("invlaid traingle")'''
'''
#7. Find the greatest among three numbers
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))

if a>=b and a>=c:
    print(a,"Greatest among three numbers")
elif b>=a and b>=c:
    print(b,"Greatest among three numbers")
else:
    print(c,"Greatest among three numbers")
'''

'''#8. Check if a year is a century year and leap year

n= int(input("Enter the number: "))

if n%400==0 or n%4==0 or n%100!=0:
    print("Century leap year")
'''

'''#9. Check if a character is a digit

n=input("enter the alphabet: ")

if n.isdigit():
    print("Digit")
else:
    print("not a Digit")'''

'''#10. Check if a number is palindrome (integer)
n=input("enter the number: ")

if n == n[::-1]:
    print("palindrome")'''

'''#11. Compare lengths of two strings
n=input("enter the value: ")
t=input("enter the value: ")

if len(n)>len(t):
    print("first string is longer")
else:
    print("Second string is longer")'''


'''#12. Check if a number is within a specific range (50 to 100) and divisible by 5
n=int(input("enter the number: "))

if 50<n<100 and n%5==0:
    print("In range and divisible by 5")
'''
'''
#13. Validate if a password length is strong (8 or more characters)

password= input("Enter the Password:")

if len(password)>8:
    print("Strong password")
else:
    print("weak password")
'''

'''
#password
password= input("Enter the Password:")

upper=lower=digit=symbol=0

for ch in password:
    if ch.isupper():
        upper=True
    elif ch.islower():
        lower=True
    elif ch.isdigit():
        digit=True
    else:
        symbol=True

if len(password)<8:
    print("Password is less than 8 digits")
elif upper == 0:
    print("Mention at least one uppercase letter")
if len(password)>8 and upper and lower and digit and symbol:
    print("strong password")
else:
    print("Weak password")


'''

'''#15. Check if the character is a special symbol (!, @, #, etc.)

n=input("Enter the character:")

if not n.isalnum():
    print("Special character")'''

'''#16. Check if temperature is cold (<15°C), moderate (15–30°C), or hot (>30°C)

n=int(input("enter the number:"))

if n<15:
    print("temperature is cold")
elif 15<n<30:
    print("moderate")
else:
    print("hot")
'''

'''#17. Check if a number lies outside the range 10 to 50

n=int(input("Enter the number: "))

if 10<n<50:
    print("number lies outside the range 10 to 50")
    '''




'''#18. Check if number is a perfect square

n = int(input("Enter a number: "))

i = 1

while i * i <= n:
    if i * i == n:
        print("Perfect square")
        break
    i += 1
else:
    print("Not a perfect square")'''


'''#19. Compare two ages and determine who is older or if same age
n = int(input("Enter a number: "))
t= int(input("Enter a number: "))

if n>t :
    print("n is older ")
elif t>n:
    print("t is older")
else:
    print("both ages are same")'''
'''
#20. Check if an angle is acute, right, or obtuse
n=int(input("Enter the number:"))

if n<90:
    print("acute angle")

elif n==90:
    print("right angle")

else:
    print("obtuse angle")'''
