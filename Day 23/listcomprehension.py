
'''# list comprehension
l=[]
for i in range(1,11):
    l.append(i)
print(l)

res=[i for i in range(1,11)]
print(res)

l=[]
n=12
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(l)

n=12
res=[i for i in range(1,n+1) if n%i==0]
print(res)

l=[]
r=[12,23,45,687,34,123,12,43,90]
for i in r:
    if i%2==0:
        l.append(i)
    else:
        l.append(0)
print(l)

r=[12,23,45,687,34,123,12,43,90]
res=[i if i%2==0 else 0 for i in r]
print(res)


#r=[[12,23,45],[687,34,123],[12,43,90]]
for i in r:
    l=[]
    for j in i:
        if j%2==0:
            l.append(j)



r=[[12,23,45],[687,34,123],[12,43,90]]
res=[j for i in r for j in i if j%2==0]
print(res)

#set 
res={i for i in range(1,11)}
print(res)

n=12
res={i for i in range(1,n+1) if n%i==0}
print(res)

r=[12,23,45,687,34,123,12,43,90]
res={i if i%2==0 else 0 for i in r}
print(res)


r=[[12,23,45],[687,34,123],[12,43,90]]
res={j for i in r for j in i if j%2==0}
print(res)'''

'''
l=[]
for i in range(10):
    n=int(input())
    l.append(i)

l=[int(input(f"enter the number-{i+1}: "))for i in range(10)]
print(l)
'''
'''names=[input(f"enter the name -{name+1}: ")for name in range(5)]
print(names)
'''
'''names={input(f"enter the name -{name+1}: "):int(input("enter the marks: "))for name in range(5)}
print(names)'''

res={i:i*i for i in range(1,10+1)}
print(res)