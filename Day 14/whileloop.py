#while: exicute until and unless we need contiition True

#in while loop you have 3things starting value ,when to stop,update
#1. 1to 10 numbers
'''i=1
while i <=10:
    print(i)
    i+=1

#2.Reverse 10 to 0
i=10
while i>0:
    print(i)
    i -=1

#3.even numbers 2 to 100
i=2
while i<=100:
    print(i,end=",")
    i +=2 #iterations we need is 2


#4.iteate a stirng 
#we can iterate string,lsit,tuple we cant itearte set,dict there is no index value

s="Python Programming"

i=len(s)-1
while i>=0:
    print(s[i],end="")
    i-=1'''


#5.list,remove the zeros,print(l)

'''l=[1,0,0,0,2,3,4,5,56,12,0,13,0,0,0,16,0]
while 0 in l:
    l.remove(0)
print(l)'''
#nevr ever work on rmeove the index values in removing 


'''
#6.input product,exit,price


dict={} #empty dict
total_bill=0
#while condtion is true
while True:
    product=input("Enter the product (for exit): ")
    #run this untill user click exit
    if product == 'exit':
        break
    price= int(input("Enter the Price: "))

    total_bill+=price
    dict[product]=price

print(dict)
print("Total Bil:",total_bill)  '''  

'''dict={}
total_bill=0
while True:
    product=input("Enter the product (for exit): ")
    if product == 'exit':
            break
    price =int(input("Enter the price: "))

    total_bill +=price
    data[product]=price

print(dict)
print("Total Bil:",total_bill) '''




#while True --->it goes infinetlty
#while with else
'''i=0
while i<=10:
    i+=1
    if i==15:
        break
    print(i)
else:
    print("End of the loop")
'''
#finally
#done with loops and all

#HOME WORK
#hold and  completee remaining#8,9,11,14,17,20



'''def washing_clothes():
    clothes_dirty=True

    while clothes_dirty:
        print("washing")

    #after
    clothes_dirty=False

print("clothes are clean")'''

#1.'''print 1 to 10'''
'''
i=1
while i<=10: #<10 1,2,3,4,5,6,7,8,9 only print i<=10 1 to 10 print #But i starts at 1.
    print(i)
    i+=1'''


#2.Print numbers from 10 to 1

'''i=10
while i>=1:
    print(i)
    i-=1
'''

    
#3.product of digits

'''def product_display(n):
    product=1

    while n>1:
        digit=n%10
        product+=product*digit
        n=n//10
    
    return product 




n=int(input("Enter the number"))
print(product_display(n))'''



#4.“Find the product of two numbers using a function”
def product_display(a,b):
    return a*b
