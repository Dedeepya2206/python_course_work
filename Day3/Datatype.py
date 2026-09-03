Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> count=10
>>> count=20
>>> count
20
>>> #float
>>> price=99.9
>>> price
99.9
>>> type(price)
<class 'float'>
>>> #complex
>>> c=4+9j
>>> c
(4+9j)
>>> c=4+9J
>>> c
(4+9j)
>>> type(c)
<class 'complex'>
>>> count=10
>>> #seqencial type
>>> #string
>>> s='Dedeepya'
>>> type(s)
<class 'str'>
>>> #list
>>> s=[1,2,3]
>>> #empty list
>>> l=[]
>>> l=list() #consturoctor
>>> type(l)
<class 'list'>
>>> l=[1,2,2,4,4,5,"deepu",56.7,89.0,[1,2,3],(1,2)]
>>> l
[1, 2, 2, 4, 4, 5, 'deepu', 56.7, 89.0, [1, 2, 3], (1, 2)]
>>> #tuple use()
>>> t=()
>>> t=tuple()
>>> t=(1,2,3,"Deepu", [1,2,36],{1,2,3,6},True,False)
>>> t
(1, 2, 3, 'Deepu', [1, 2, 36], {1, 2, 3, 6}, True, False)
>>> #tuple is immutable, use for fixed data type,allow duplicates
>>> t=(1,1,1,2,2)
>>> t
(1, 1, 1, 2, 2)
>>> #mapping data type
>>> #set
>>> s={}
>>> typeof(s)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    typeof(s)
NameError: name 'typeof' is not defined
>>> type(s)
<class 'dict'>
>>> s=set()#constructor
>>> s={1,2,3,4,"Harusha",34.9,67.10}
>>> s
{1, 2, 3, 4, 34.9, 67.1, 'Harusha'}
>>> type(s)
<class 'set'>
>>> s={1,2,2}
>>> s
{1, 2}
>>> #set is a mutable,unorder,no duplicate,has dynamic sized
>>> #dict is a key value pair ,is a collections of items,{},order, key has no duplicate,value has duplicates,mutable
>>> d={}
>>> type(d)
<class 'dict'>
>>> d={'id':01, 'Name':'Deepu'}
SyntaxError: invalid token
>>> d={'id':1,"Name':'Dedeepya}
   
SyntaxError: EOL while scanning string literal
>>>  d={'id':1, 'Name':'Deepu'}
 
SyntaxError: unexpected indent
>>> d={'id':01, 'Name':'Deepu'}
SyntaxError: invalid token
>>> d={'id':1, 'Name':'Deepu'}
>>> d
{'id': 1, 'Name': 'Deepu'}
>>> #boolean
>>> status=False
>>> type(status)
<class 'bool'>
>>> #None  when we are un sure about value we will got to none
>>> status=None
>>> type(status)
<class 'NoneType'>
>>> #frozenset we can not add or remove data it is a unique value
>>> s=frozen({1,3,5,6})
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s=frozen({1,3,5,6})
NameError: name 'frozen' is not defined
>>> s=frozen([1,4,5,6])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s=frozen([1,4,5,6])
NameError: name 'frozen' is not defined
>>> s=frozenset([1,4,5,6])
>>> s
frozenset({1, 4, 5, 6})
>>> 