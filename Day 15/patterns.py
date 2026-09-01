#row-->horizontal
#coloums-->vertical
#print()-->i want my output itertions in one after another next line
#outside the outer loop


for i in range(20):
    for j in range(10):
        print('*',end= " ")
    print()


for i in range(5):
    for j in range(5):
        print('*',end= " ")
    print()


for row in range(5):
    for col in range(5):
        print(row,end= " ")
    print()

for row in range(5):
    for col in range(5):
        print(col,end= " ")
    print()

for i in range(5):
    for j in range(5):
        print(i+j,end=" ")
    print()

'''#output in T or F
for i in range(5):
    for j in range(5):
        print(j%2==0,end=" ")
    print()'''

'''for i in range(5):
    for j in range(5):
        print((i+j)%2,end=" ")
    print()
'''

'''for i in range(5):
    #col is changing 0 -1 ,1-2,2-3
    for j in range(i+1):
        print('*',end=" ")
    print()'''

#7 j=len(n)-i
for i in range(5):
    for j in range(5-i):
        print('*',end=" ")
    print()
