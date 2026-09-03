'''for i in range(1,10):
    if i==15:
        break
    print(i)
else:
    print("end of the loop")
    '''
'''pin=1234
for _ in range(5):
    epin=int(input("enter the pin: "))
    if pin==epin:
        print("unlock phone")
        break
    else:
        print("invalid pin")
else:
    print("Try after 30 seconds")
    '''
'''n=int(input("enter the number: "))
print("Factors: ",end=" ")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
        '''
'''#prime number
n=int(input("enter the number: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
        c+=1
if c==2:
    print("prime")
else:
    print("not prime number")
    '''
'''n=int(input("enter the number: "))
c=0
for i in range(2,n+1):
    if n%i==0:
        print(i,end=" ")
        c+=1
if c==1:
    print(" prime")
else:
    print("not prime number")
    '''
'''n=int(input("enter the number: "))
c=0
for i in range(1,n):
    if n%i==0:
        print(i,end=" ")
        c+=1
if c==1:
    print(" prime")
else:
    print("not prime number")
    '''
'''n=int(input("enter the number: "))
c=0
for i in range(1,n//2+1):
    if n%i==0:
        print(i,end=" ")
        c+=1
if c==0:
    print("prime")
else:
    print("not prime number")
    '''
'''n=int(input("enter the number: "))
for i in range(2,n//2+1):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime number")
    '''