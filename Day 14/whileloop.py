#while
'''i=1
while i<=10:
    print(i)
    i+=1
'''
'''
i=10
while i>0:
    print(i)
    i-=1
   '''
'''
#even numbers
i=2
while i<=100:
    print(i,end=" ")
    i+=2
'''
'''
#reverse of a string using while
s="Codegnan"
i=len(s)-1
while i>=0:
    print(s[i],end="")
    i-=1
    '''
'''l=list(map(int,input().split()))
while 0 in l:
    l.remove(0)
print(l)
'''
'''d={}
bill=0
while True:
    product=input("Enter the product (for exit): ")
    if product =="exit":
        break
    price=int(input("Enter the price: "))
    bill+=price
    d[product]=price
print(d)
print("Total bill: ",bill)
'''
'''i=0
while i<=10:
    i+=1
    if i==5:
        break
    print(i)
else:
    print("end of the loop")
    '''
'''i=0
while i<=10:
    i+=1
    if i==15:
        break
    print(i)
else:
    print("end of the loop")
    '''