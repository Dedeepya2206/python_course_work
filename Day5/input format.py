Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''int-int(intput())
float-float(input())
str-input()
list of str - input().split()
list of int -list(map(int,input().split()))
list of float-list(map(float,input().split()))

tuple of str - input().split()
tuple of int -list(map(int,input().split()))
tuple of float-list(map(float,input().split()))

set of str - input().split()
set of int -list(map(int,input().split()))
set of float-list(map(float,input().split()))'''
'int-int(intput())\nfloat-float(input())\nstr-input()\nlist of str - input().split()\nlist of int -list(map(int,input().split()))\nlist of float-list(map(float,input().split()))\n\ntuple of str - input().split()\ntuple of int -list(map(int,input().split()))\ntuple of float-list(map(float,input().split()))\n\nset of str - input().split()\nset of int -list(map(int,input().split()))\nset of float-list(map(float,input().split()))'
>>> x=input()
abvcd
>>> x
'abvcd'
>>> x=input("enter a value ::")
enter a value ::hjiuhi
>>> x
'hjiuhi'
>>> x=int(input("Enter a value:"))
Enter a value:1 2 34
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x=int(input("Enter a value:"))
ValueError: invalid literal for int() with base 10: '1 2 34'
>>> x=int(input("enter a value "))
enter a value 1234
>>> x
1234
>>> x=float(input("enter a value "))
enter a value 12 34 56
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x=float(input("enter a value "))
ValueError: could not convert string to float: '12 34 56'
>>> x=float(input("enter a value "))
enter a value 1234
>>> x
1234.0
>>> x=intput("enter a value:").split()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x=intput("enter a value:").split()
NameError: name 'intput' is not defined
>>> x=input("enter a value : :").split()
enter a value : :deepu
>>> x
['deepu']
>>> x=input("enter a value : :").split()
enter a value : :deepu pallavi harsha nisha
>>> x
['deepu', 'pallavi', 'harsha', 'nisha']
>>> x=input("enter a value : :").split()
enter a value : :1 2 3 4 56
>>> x
['1', '2', '3', '4', '56']
>>> x=list(map(int,input("Enter avalue :").split()))
Enter avalue :1 2 3 45 67 897
>>> x
[1, 2, 3, 45, 67, 897]
>>> x=list(map(float,input("Enter avalue :").split()))
Enter avalue :2 3 45 678 989
>>> x
[2.0, 3.0, 45.0, 678.0, 989.0]
>>> x=tuple(map(int,input("Enter avalue :").split()))
Enter avalue :23 5 6 7 81
>>> x
(23, 5, 6, 7, 81)
>>> x=list(map(float,input("Enter avalue :").split()))
Enter avalue :56 78 4 2 39
>>> x
[56.0, 78.0, 4.0, 2.0, 39.0]
>>> x=input("enter a value :").split()
enter a value :deepu pallavi
>>> x
['deepu', 'pallavi']
>>>  x=tuple(map(float,input("Enter avalue :").split()))
 
SyntaxError: unexpected indent
>>> x=list(map(float,input("Enter avalue :").split()))
Enter avalue :56 78 4 2 39
>>> x=input("enter a value :").split()
enter a value :23 54 67
>>> x
['23', '54', '67']
>>> x=set(input("enter a value :").split())
enter a value :deepu pallavi
>>> x
{'deepu', 'pallavi'}
>>> x=set(map(int,input("Enter avalue :").split()))
Enter avalue :1 2 3 4
>>> x
{1, 2, 3, 4}
>>> x=set(map(float,input("Enter avalue :").split()))
Enter avalue :35 67 89 24
>>> x
{24.0, 89.0, 67.0, 35.0}
>>>  x=tuple(input("enter a value :").split())
 
SyntaxError: unexpected indent
>>> x=set(input("enter a value :").split())
enter a value :deepu ishu pllavi
>>> x
{'deepu', 'pllavi', 'ishu'}
>>> a,b=[1,2]
>>> a
1
>>> b
2
>>> a,b=(1,2)
>>> a
1
>>> b
2
>>> email,password=input().split()
dedeepya@gmail.com 123deppu
>>> email
'dedeepya@gmail.com'
>>> password
'123deppu'
>>> #sides of triangle
>>> a,b,c=list(map(int,input("enter a side:").split())
	   )
enter a side:1 2 4
>>> a
1
>>> b
2
>>> c
4
>>> name, marks=input().split()
dedeepya
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    name, marks=input().split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> dedeepya 89
SyntaxError: invalid syntax
>>> name,marks = input().split()
dedeepya 89
>>> name
'dedeepya'
>>> marks
'89'
>>> int(marks)
89
>>> #eval fn
>>> e=eval(input())
1234 567
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    1234 567
           ^
SyntaxError: unexpected EOF while parsing
>>> e=eval(input())
1
>>> e
1
>>> e=eval(input())
True
>>> e
True
>>> e=eval(input())
{1: 1,2: 2,3: 3}
>>> e
{1: 1, 2: 2, 3: 3}
>>> e=eval(input())
"Dedeepya"
>>> e=eval(input())
[1,2,3,"Deepu",[1,23,4]]
>>> e
[1, 2, 3, 'Deepu', [1, 23, 4]]
>>> e=eval(input())
(1,2,3,45)
>>> e
(1, 2, 3, 45)
>>> e=eval(input())
123
>>> e
123
>>> e=eval(input())
123.78
>>> e
123.78
>>> e=eval(input())
{1,2,3}
>>> e
{1, 2, 3}
>>> 