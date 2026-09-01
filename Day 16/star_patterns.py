'''
n=int(input("enter size: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

n=int(input("enter a size :"))
for i in range(n):
    for sp in range (n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

n=int(input("enter the size:"))
for i in range(n):
    for sp in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()

n=int(input('enter the size:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

n=int(input("enter a size:"))
for i in range(n):
    for j in range(n):
        
        if i==0 or j==0 or i==n-1 or j==n-1 or i==n//2 or j==n//2: # if i==0 or j==0 i%2==0 or j%2==0
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=int(input("enter a size:"))
for i in range(n):
    for j in range(n):
        if (i==j or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#TO print A
n = int(input("enter a size:"))

for i in range(n):
    for j in range(2 * n - 1):
        if (j == n - 1 - i) or (j == n - 1 + i) or (i == n // 2 and n - 1 - i < j < n - 1 + i):
            print("*", end="")
        else:
            print(" ", end="")
    print()

#To print A
n=int(input("enter a size:"))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n//2 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# to printy G
n=int(input("enter a size:"))
m=n//2
for i in range (n):
    for j in range(n):
        if (i==0 or j==0 or(i==n-1 and j<=m)or(j==m and i>=m)or(i==m and j>=m)or (j==n-1 and i>=m)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# To print B
n=int(input("enter a size: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n//2 or j==n-1 or i==n-1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# To print C
n=int(input("enter a size: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#To print D
n=int(input("enter a size: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#To print E 
n=int(input("enter a size: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or i==n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#To Print K
n=int(input("enter a size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or(i==m and j<=m) or (i+j==n-1 and i<=m) or (i==j and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# To Print M
n=int(input("enter a size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i+j==n-1 and i<=m) or (i==j and i<=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# To print F
n=int(input("enter a value: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n//2  ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#print H
n=int(input("enter size:"))
for i in range(n):
    for j in range(n):
        if (j==n-1 or j==0 or i==n//2):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()

# To print I
n=int(input("enter a size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#To print J
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or (j == n-1 and i < n-1) or (i == n-1 and j < n-1) or (j == 0 and i == n-2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

#To print L
n=int(input("enter a size:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# To print N
n=int(input("enter a size:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#To do O
n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if (i == 0 or i == n-1 or j == 0 or j == n-1) and \
           not ((i == 0 and j == 0) or
                (i == 0 and j == n-1) or
                (i == n-1 and j == 0) or
                (i == n-1 and j == n-1)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# To print P
n=int(input("enter a size:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or j==n or i==n//2 or n//2>i>=n-j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#To print Q
n=int(input(" enter a size:"))
for i in range(n):
    for j in range(n):
        if ((i == 0 or i == n-2) and (0 < j < n-1)) or ((j == 0 or j == n-1) and (0 < i < n-2)) or (i == j and i >= n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# To print R
n = int(input("Enter size: "))
mid = (n - 1) // 2
for i in range(n):
    for j in range(n):
        if (j == 0 or i == 0 or
            i == mid or (j == n-1 and 0 < i < mid) or(i - mid == j and i > mid)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#To print S
n=int(input("Enter a size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if ((i==0 or i==n-1 or i==m ) and (j<n))or (j==0 and i<m or j==n-1 and i>m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# To print T
n=int(input("Enter a value: "))
for i in range(n):
    for j in range (n):
        if i==0 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#To print U
n=int(input("enter a size:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#To print W
n=int(input("enter a size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i+j==n-1 and j<=m) or (i==j and j>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#To print X
n=int(input("enter a size:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#To print Y
n=int(input("Enter a size:"))
for i in range(n):
    if i < n // 2:
        print(" " * i + "*" + " " * (n - 2*i - 2) + "*")
    else:
        print(" " * (n// 2) + "*")

# To print Z
n=int(input("enter a size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==n-j-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# To print Y
n=int(input("enter a size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or (i+j==n-1 and i<=m) or (j==m and i>=m) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#To print V
n=int(input("enter a size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m)  or (j==n-1 and i<=m)  or (i-j==m and i>=m) or (i+j==m+n-1 and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()