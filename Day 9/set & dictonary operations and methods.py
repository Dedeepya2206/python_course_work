Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={}
type(s)
<class 'dict'>
s=set()
s={1,2,3,4,12,324,9876,34,123421}
s
{1, 2, 3, 4, 34, 324, 12, 9876, 123421}
s=set()
s
set()
s.add(1)
s.add(1.2)
s.add(2+4j)
s
{1, 1.2, (2+4j)}
s.add("str")
s
{1, 'str', 1.2, (2+4j)}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.addd((1,2,3))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.addd((1,2,3))
AttributeError: 'set' object has no attribute 'addd'. Did you mean: 'add'?
s.add((1,2,3))
s
{1, 'str', 1.2, (1, 2, 3), (2+4j)}
s.add({1:2})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.add({1:2})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
a={1,2,3,4,5}
b={3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a|b
{1, 2, 3, 4, 5, 7, 9}
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a&b
{3, 5}
a.intersection(b)
{3, 5}
a-b
{1, 2, 4}
a^b
{1, 2, 4, 7, 9}
a
{1, 2, 3, 4, 5}
#{1}{2}{3}{4}{5}{1,2}{3,4}{4,5}{1,3}{4,1}{1,2,3,4,5}
a
{1, 2, 3, 4, 5}
{1}<=a
True
{1,2,3,4}<=a
True
a
{1, 2, 3, 4, 5}
{1,2,3,4,5}<=a
True
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a.isdisjoint(b)
False
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.issubset(b)
False
a.superset(b)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.superset(b)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
a.issuperset(b)
False
a
{1, 2, 3, 4, 5}
5 in a
True
10 not in b
True
7 in b
True
#set methods
a
{1, 2, 3, 4, 5}
min(a)
1
max(a)
5
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
a
{1, 2, 3, 4, 5}
b.adda(12)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b.adda(12)
AttributeError: 'set' object has no attribute 'adda'. Did you mean: 'add'?
b.add(12)
b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c=a.copy()
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12}
a.add(123)
a
{1, 2, 3, 4, 5, 123, 12}
a.update({16,34,56})
a
{1, 2, 3, 4, 5, 34, 12, 16, 56, 123}
a.pop()
1
a.pop()
2
a.pop()
3
a
{4, 5, 34, 12, 16, 56, 123}
a.remove(56)
a
{4, 5, 34, 12, 16, 123}
a.remove(56)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.remove(56)
KeyError: 56
a.discard(56)
a
{4, 5, 34, 12, 16, 123}
a.discard(12)
a
{4, 5, 34, 16, 123}
a.clear()
a
set()
a={1,2,3}
a.update({2.3,"str",2+3j,-1,})
a
{1, 2, 3, 'str', 2.3, (2+3j), -1}
len(a)
7
all(a)
True
any(a)
True
#frozen set
a=frozenset({1,12,13,14,59,20})
a
frozenset({1, 20, 59, 12, 13, 14})
#dictonary
d={]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2','k3':'v3'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
2282590608128
d['k4]='v4'
  
SyntaxError: unterminated string literal (detected at line 1)
d['k4']='v4'
  
d['k4']='v4'
  
d
  
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
id(d)
  
2282590608128
d['k1']='v11'
  
d
  
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d['k5']='v4'
  
d
  
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v4'}
d={}
  
d[1]='int'
  
d
  
{1: 'int'}
d=[12.3]='flt'
  
SyntaxError: cannot assign to literal
d[12.3]='flt'
  
d
  
{1: 'int', 12.3: 'flt'}
d[12+3j]='com'
  
d
  
{1: 'int', 12.3: 'flt', (12+3j): 'com'}
d["str"]='string'
  
d
  
{1: 'int', 12.3: 'flt', (12+3j): 'com', 'str': 'string'}
d[[1,2,3]='list'
  
SyntaxError: invalid syntax
d[[1,2,3]]='list'
  
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[(1,2,3,4)]='tuple'
  
d
  
{1: 'int', 12.3: 'flt', (12+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d={}
  
d[1]=1
  
d[2]=12.3
  
d[3]=12+4j
  
d[4]='str'
  
d[5]=[1,2,3,4]
  
d[6]=(1,2,3)
  
d[7]={1,2,3}
  
d[8]={1:1}
  
d[9]=True
  
d
  
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
d={1: 'int', 12.3: 'flt', (12+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
  
d
  
{1: 'int', 12.3: 'flt', (12+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d[False]='False'
  
d
  
{1: 'int', 12.3: 'flt', (12+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple', False: 'False'}
d[frozenset{1,2,3}]='fset'
  
SyntaxError: invalid syntax. Perhaps you forgot a comma?
KeyboardInterrupt
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
  
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
d={1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
  
d
  
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
9 in d
  
True
10 in d
  
False
'str' in d
  
False
d[5]
  
[1, 2, 3, 4]
d[8]
  
{1: 1}
>>> d[10]
...   
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    d[10]
KeyError: 10
>>> d.get(10)
...   
>>> d.get(1)
...   
1
>>> d.get(10,"key is not present")
...   
'key is not present'
>>> d.get(6,"key is not present")
...   
(1, 2, 3)
>>> d
...   
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[3]=4
...   
>>> d
...   
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[5]=10
...   
>>> d
...   
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[6]=12
...   
>>> d
...   
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[7]=20
...   
>>> d
...   
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: 12, 7: 20, 8: {1: 1}, 9: True}
