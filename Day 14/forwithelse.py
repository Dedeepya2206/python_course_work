#when theere is brreak stat in my for loop the else will never exicute(break ,np else)
#when there is no break stat in my for loop the else will exicute(no break, else )



#break -->else never exicute
#no break--->else exicute 
#aug 17th 


for i in range(1,10):
    if i==5:
        break
    print(i)
else:
    print("End of the loop")

#use cse of for with else




#2.phone unlock

#for iterating 5 times i am using but i dont have use of i then_
#else for ki petam beacuse wrong password 5 times kante kodithe try after 30sec
'''
pin=1234

for _ in range(5):
    epin = int(input("Enter the pin: "))
    if pin == epin:
        print("unlock the phone")
        break
    else:
        print("Invalid password")

else:
    print("Try after 30seconds")
'''

#3.prime number :a number is divisble by one and itself
# a number which having 2 factors whuch is one and itself


#LOGIC TO FIND FACTORS OF A NUMBER 

'''n=int(input("Enter the number: "))
print("Factors: " ,end=" ")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")'''

#if count==2 it is prime number else not a prime number
'''
n = int(input("enter the number: "))
c=0

for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("Prime Number")
else:
    print("not a prime number")
    '''

'''#without using count we just optimized the code

n= int(input("Enter the number: "))

for i in range(2,n//2+1): #2,12//3
    if n%i==0:
        print("Not Prime Number")
        break
else:
    print("Prime Number")

'''
