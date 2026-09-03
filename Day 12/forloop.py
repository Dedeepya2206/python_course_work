#str list tuple set dict range()
'''
for var in seq:
    print(var)'''
'''s="Codegnan"
for ch in s:
    if ch in "aeiouAEIOU":
        print(ch)
'''
'''s="Codegnan"
for ch in s:
    print(ch)
    '''
'''l=[1,2,3,4,5,67,87,54,98,69,78]
for i in l:
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")
'''
'''marks=(90,65,20,45,92,56,70)
for m in marks:
    if m>35:
        print(m,"pass")
    else:
        print(m,"odd")
        '''
'''followers={"harsha","nandhu","kala","hari","pandu","aruna"}
for i in followers:
    print(i)
    '''
'''
bus={"s1":"booked","s2":"available","s3":"available","s4":"available"}
for s in bus:
    if bus.get(s)=="available":
        print(s,bus.get(s))
        '''
#range syntax->(start,end+1,step)=>default values are (0,nodef,1)
'''for i in range(1,11):
    print(i)
    '''
'''for i in range(1,11):
    print(i,end=" ")
    '''

'''for i in range(2,51,2):
    print(i,end=" ")
    '''
'''for i in range(1,100,2):
    print(i,end=" ")
    '''
'''for i in range(5,51,5):
    print(i,end=" ")
    '''
'''n= int(input())
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
    '''
