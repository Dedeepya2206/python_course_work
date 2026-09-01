'''
def funname(parameters):
    #statements
    #return(optional)
funname(values)


def display(name,email,password):
    print(f'Hello {name}')
    print(f'Your email:{email}')
    print(f'your password:{password}')
display("Dedeepya","dedeepya@gmail.com","deepu123")
display("Pallavi","pallavi@gmail.com","pallavi123")

#Leap Year or not
def isleapyear(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
for year in range(2001,2027):
    isleapyear(year)



#sum of digits
def sumofdigits(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    return sum
n=int(input("enter the numbers :"))
print(f"sum of {n} digits is {sumofdigits(n)}")

def productofdigits(n):
    product=1
    while n>0:
        product*=n%10
        n=n//10
    return product
n=int(input("enter the numbers :"))
print(f"product of {n} digits is {productofdigits(n)}")

#To print the strong password or weak password
def checkpassword(password):
    if len(password)>8:
        check=set()
        for i in password:
            if i.isupper():
                check.add("u")
            elif i.islower():
                check.add("l")
            elif i.isdigit():
                check.add("d")
            else:
                check.add("s")
        if len(check)==4:
            return "Strong Password"
    return "Weak Password"
password=input("Enter the password:")
print(checkpassword(password))#print(f"password is {checkpassword(password)}")

# To print the table of a number 
def table(n):
    print(f'--------Table - {n}----------')
    for i in range(1,11):
        print(f" {n} * {i} = {n*i}")
for i in range(1,21):
    table(i)
'''