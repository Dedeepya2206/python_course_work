'''s="python programming"
for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
        print(i,s[i])
        '''
'''l=[2,3,5,6,1,4]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        print(i,l[i])
        sum+=i
print("sum:",sum)
'''
'''n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"factorial of {n} id {fact}")
'''
'''data={}
n=int(input("enter the no of students: "))
max_marks=0
for i in range(n):
    name=input("enter the name: ")
    marks=int(input("Enter the marks: "))
    if marks>max_marks:
        max_marks=marks
    data[name]=marks
print(data)
print("Maximum Marks: ",max_marks)
'''

bill=0
n=int(input("enter no of items:"))
data={}
for i in range(1,n+1):
    product=input(f"product - {i}: ")
    price=int(input(f"price - {i}: "))
    quantity=int(input(f"quantity - {i}: "))
    r=quantity*price
    bill+=r
    data[product]=f'{price}*{quantity}={r}'
print(data)
print(bill)