'''
#To print sum of 2 numbers
def sumofnumbers(a,b):
    return a+b
sum=sumofnumbers(10,20)
print(f"The sum is : {sum}")

#To print square of a number
def squareofnumber(n):
    return n*n
n=int(input("Enter the number:"))
print(f"The square is: {squareofnumber(n)}")

#To print area of a circle
def areaofcircle(r):
    return 3.14*r*r
n=int(input("Enter a radius :"))
print(f"The area of circle is : {areaofcircle(n)}")

# To Greet the user
def display(name):
    print(f'Hello {name}')
user_name=input("Enter the name :")
display(user_name)

#To convert celsius to fahrenheit
def celsius_to_fahrenheit(c):
    return (c*9/5)+32
c=int(input("Enter the temperature in celsius:"))
print(f"Temperature in Fahrenheit : {celsius_to_fahrenheit(c)}")
'''
#To print product of 3 numbers
def product(a,b,c):
    return a*b*c
a=int(input("enter 1st numbers: "))
b=int(input("enter 2nd numbers: "))
c=int(input("enter 3rd numbers: "))
print(f"The product is : {product(a,b,c)}") 
