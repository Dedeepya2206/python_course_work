Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Conversion of Data Types
>>> #Interger to other Data Types
>>> a=10
>>> type(a)
<class 'int'>
>>> float(a)
10.0
>>> str(a)
'10'
>>> bool(a)
True
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> complex(a)
(10+0j)
>>> #so that integer can only convert to float,complex,string,bool,complex. Where as set,list,tuple are the collection of elements we can not convert, and dict is a key value pair
>>> #float
>>> f=19.08
>>> type(f)
<class 'float'>
>>> int(f)
19
>>> str(f)
'19.08'
>>> bool(f)
True
>>> complex(f)
(19.08+0j)
>>> list(f)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
>>> set(f)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
>>> tuple(f)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
>>> dict(f)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
>>> #hence so that the float only convert into int,str,bool,complex.Where as set,list,tuple are the collection of elements we can not convert, and dict is a key value pair.
>>> #string
>>> s='deepu'
>>> type(s)
<class 'str'>
>>> int(s)#here we can convert beacuse the value of s is character not a number
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(s)#here we can convert beacuse the value of s is character not a number
ValueError: invalid literal for int() with base 10: 'deepu'
>>> x=10#here we can convert it into string because it can make it in ""
>>> int(x)
10
>>> #same for float if we have number values it will work unelse  a oppisite values.
>>> float(x)
10.0
>>> bool(x)
True
>>> complex(x)
(10+0j)
>>> list(x)#list is a collection of characters so it will convert
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list(x)#list is a collection of characters so it will convert
TypeError: 'int' object is not iterable
>>> list(s)
['d', 'e', 'e', 'p', 'u']
>>> set(s)#also collection of characters
{'d', 'u', 'p', 'e'}
>>> tuple(s)#same as followed
('d', 'e', 'e', 'p', 'u')
>>> dict(s)#it is not a key value pair
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    dict(s)#it is not a key value pair
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> #list
>>> l=[2,3,4,'ddd']
>>> l
[2, 3, 4, 'ddd']
>>> type(l)
<class 'list'>
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a number, not 'list'
>>> string(l)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    string(l)
NameError: name 'string' is not defined
>>> str(l)
"[2, 3, 4, 'ddd']"
>>> set(l)
{2, 3, 4, 'ddd'}
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
>>> complex(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> #so in the list we can only convert string,set,tuple
>>> #tuple can only convert to str,list,set,bool,complex
>>> t=()
>>> type(t)
<class 'tuple'>
>>> t=(a,b,c,1,2,3)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    t=(a,b,c,1,2,3)
NameError: name 'b' is not defined
>>> t=(23,4,5)
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> str(t)
'(23, 4, 5)'
>>> list(t)
[23, 4, 5]
>>> set(t)
{4, 5, 23}
>>> complex(t)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> float(t)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a number, not 'tuple'
>>> complex(t)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> bool(t)
True
>>>s={1,2,3}
