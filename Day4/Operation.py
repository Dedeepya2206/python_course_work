Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #arthematic Operator
>>> a=20
>>> b=10
>>> a+b
30
>>> a-b
10
>>> a*b
200
>>> a/b
2.0
>>> a//b
2
>>> a%b
0
>>> a**b
10240000000000
>>> #In Arthematic operator we have +,-,*, /, //, %, **.
>>> #Comparision Operator =,!=,>,<,>=,<=,==.
>>> a=10,b=20
SyntaxError: can't assign to literal
>>> a=20
>>> b=10
>>> a+b
30
>>> a-b
10
>>> a==b
False
>>> a!=b
True
>>> a>b
True
>>> a<b
False
>>> a>=b
True
>>> a<=b
False
>>> Assignment Operators
SyntaxError: invalid syntax
>>> #Assignment Operators
>>> # =,+=,-=,*=,/=,\\=,%=,**=,&=,|=,^=.
>>> c=10
>>> c=c+10
>>> c
20
>>> c+=10
>>> c
30
>>> c-=10
>>> c
20
>>> c*=10
>>> c
200
>>> c/=10
>>> c
20.0
>>> c//=2
>>> c
10.0
>>> c%=2
>>> c
0.0
>>> c+=10
>>> c
10.0
>>> c**=2
>>> c
100.0
>>> c^=2
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c^=2
TypeError: unsupported operand type(s) for ^=: 'float' and 'int'
>>> #Relational Operators
>>> n=10
>>> n%2==0 and n%3==0
False
>>> n%2==0 or n%3==0
True
>>> n=5
>>> n>10
False
>>> not n>10
True
>>> n%8==0 or n%3==0
False
>>> #membership Operator
>>> #string, list, tuple, set, dict,
>>> l=[1,2,3]
>>> 3 in l
True
>>> 4 in l
False
>>> 3 not in l
False
>>> t=(1,2,3,4,5)
>>> 6 in t
False
>>> 2 in t
True
>>> 1 not in t
False
>>> s={1,2,3,6,7,8}
>>> s
{1, 2, 3, 6, 7, 8}
>>> 5 in s
False
>>> 7 in s
True
>>> 4 not in s
True
>>> d={"name":'deepu',"batch":5}
>>> name in d
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    name in d
NameError: name 'name' is not defined
>>> d={'name':'deepu','batch':5}
>>> name in d
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    name in d
NameError: name 'name' is not defined
>>> 'name' in d
True
>>> 'age' in d
False
>>> #membership operator  can only consider collection of data like list, set,string,tuple,dict.
>>> #Identity Operators : Identity operators check whether two variables refer to the same object in memory.is
>>> l=[1,2,3]
>>> m=[1,2,3]
>>> l is m
False
>>> n=l
>>> n is m
False
>>> n is l
True
>>> id(n)
2384634392840
>>> #id is used to retive the memory refernce
>>> id(m)
2384634392776
>>> l is m
False
>>> l is not m
True
>>> #Mutable:which we can change in the same obj refernce,and Immutable: which we can not chnage in the same obj ref.
>>> s={1,2,3,4}
>>> id(s)
2384665288264
>>> s.add(5)
>>> s
{1, 2, 3, 4, 5}
>>> C=("Python")
>>> id(C)
2384630583536
>>> #Bitwise operator :Bitwise operators perform operations on the binary representation of numbers (0 and 1).AND &, ^XOR,NOT~,LEFT SHIFT<<,OR |,Right shift>>.
>>> 9&10
8
>>> 9|10
11
>>> 9^10
3
>>> ~85
-86
>>> 9>>10
0
>>> 9>>2
2
>>> 9<<2
36
>>> #OUTPUT STATEMENTS.
>>> a=10
>>> b-10.3
-0.3000000000000007
>>> b=10.32
>>> c="Deepu"
>>> print(a,b,c)
10 10.32 Deepu
>>> print("a value is :",a)
a value is : 10
>>> print("a value is:",a,"b value is :",b,"c value is :"c)
SyntaxError: invalid syntax
>>>  print("a value is:",a,"b value is :",b,"c value is :",c)
 
SyntaxError: unexpected indent
>>> print("a value is:",a,"b value is :",b,"c value is :"c)
SyntaxError: invalid syntax
>>> print("a value is:",a,"b value is :",b,"c value is :",c)
a value is: 10 b value is : 10.32 c value is : Deepu
>>>  print("a value is:",a,|"b value is :",b,|"c value is :",c)
 
SyntaxError: unexpected indent
>>> print("a value is:",a,"b value is :",b,"c value is :",c)
a value is: 10 b value is : 10.32 c value is : Deepu
>>> print(a,b,c)
10 10.32 Deepu
>>> print(a,b,c,sep='')
1010.32Deepu
>>> print(a,b,c,sep="\n")
10
10.32
Deepu
>>> print(a,b,c,sep="\t")
10	10.32	Deepu
>>>  print(a,b,c,sep="\t",end=@)
 
SyntaxError: unexpected indent
>>> print(a,b,c,sep="\n")
10
10.32
Deepu
>>> print(a,b,c,sep="\n",end='@')
10
10.32
Deepu@
>>> print(a,b,c,sep="\t",end='\n\n')
10	10.32	Deepu

>>> print(f'a={a} b={b} c={c}')
a=10 b=10.32 c=Deepu
>>> print(f" a value is {a}|b value is {b},|c value is {c}")
 a value is 10|b value is 10.32,|c value is Deepu
>>> a value is 10|b value is 10.32,|c value is Deepu
SyntaxError: invalid syntax
>>> print('a=%d','b=%f','c=%s'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    print('a=%d','b=%f','c=%s'%(a,b,c))
TypeError: not all arguments converted during string formatting
>>> print('a=%d, b=%f, c=%s%'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    print('a=%d, b=%f, c=%s%'%(a,b,c))
ValueError: incomplete format
>>> print('a=%d b=%f  c=%s'%(a,b,c))
a=10 b=10.320000  c=Deepu


