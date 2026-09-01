#1. Print Numbers from 1 to N (Using for loop)

n=int(input("Enter the number: "))

for i in range(1,n+1):
    print(i)



#2. Print Even Numbers from 1 to N (Using for loop)

n=int(input("Enter the number: "))

for i in range(1,n+1):
    if i%2==0:
        print(i)


#3. Sum of Numbers from 1 to N (Using for loop)

n=int(input("Enter the number: "))

sum=0

for i in range(1,n+1):
    sum=sum+i
print("sum of your number is",n)
