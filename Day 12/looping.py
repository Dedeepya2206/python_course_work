#while- dont know the iterations
#for - iterating over a sequence


#data types where we can do looping
#str,lsit,tuple,set,dict,range()

'''for var in seq:
       print(var)
'''

'''s="Codegnan"
for ch in s:
    print(ch)'''



#condition inside the loop-->to check aeiou
'''
s="codegnan"
for ch in s:
    if ch in "aeiouAEIOU":
        print(ch)'''

s="codegnan"
for ch in s:
    if ch in "aeiouAEIOU":
#How to iterate a list[condition]
'''l = [10,23,30,45,1,3,15,16,18,19,21]

for i in l:
    if i%2 == 0:
        print(i,"Even")
    else:
        print(i,"Odd")'''

'''#How to iterate a tuple(condition)
marks = (90,20,35,46,78,92,87,48)

for mark in marks:
    if mark>35:
        print(mark,"pass")
    else:
        print(mark,"fail")'''


'''#How should you iteate your set {set}
followers = {'naimisha','rani','sweety','kasula'}

for i in followers:
    print(i)'''

'''#dict

bus = {'s1':'booked','s2':'Available','s3':'Available','s4':'Available','s5':'Booked','s6':'Available'}
for seat in bus:
    if bus.get(seat)=="Available":
        print(seat,bus.get(seat))'''


#range-->will give you numaric values

'''for i in  range(1,11):
    print(i,end=" ")

#even numbers 1 -50
for i in range(2,51,2):
    print(i,end="")'''

'''#odd numbers 1-100:
for i in range(1,100,2):
    print(i,end= " ")

#5 table multiple up to 50
for i in range(5,51,5):
    print(i,end="")
'''
'''#2 table 10 steps we are using f string 
n = int(input("Enter the table no: "))
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')
'''
