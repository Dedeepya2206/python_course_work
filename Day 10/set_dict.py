Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={}
>>> s=set()
>>> s={1,2,3,4,13,14,16,9878,786,345}
>>> s
{1, 2, 3, 4, 13, 14, 16, 786, 9878, 345}
>>> s=set()
>>> s
set()
>>> s.add(1)
>>> s
{1}
>>> s.add(12.3)
>>> s
{1, 12.3}
>>> s.add(3+6j)
>>> s
{1, 12.3, (3+6j)}
>>> s.add("deepu")
>>> s
{'deepu', 1, 12.3, (3+6j)}
>>> s.add([1,23,4])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.add([1,23,4])
TypeError: unhashable type: 'list'
>>> s.add((12,34,67))
>>> s
{1, 12.3, 'deepu', (12, 34, 67), (3+6j)}
>>> l={10,20,30}
>>> m={1,2,3,4}
>>> l+m
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> #in set arthematic,indexing,slicing,repeation are not allowed.
>>> a={1,2,3,4,5,6}
>>> b={3,4,6,7,8,9}
>>> #union
>>> a |b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> a union b
SyntaxError: invalid syntax
>>> a.union b
SyntaxError: invalid syntax
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> #intersection
>>> a & b
{3, 4, 6}
>>> a.intersection(b)
{3, 4, 6}
>>> a ^b
{1, 2, 5, 7, 8, 9}
>>> a.symetric(b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.symetric(b)
AttributeError: 'set' object has no attribute 'symetric'
>>> a^b
{1, 2, 5, 7, 8, 9}
>>> a-b
{1, 2, 5}
>>> a<=b
False
>>> b<=a
False
>>> a
{1, 2, 3, 4, 5, 6}
>>> b
{3, 4, 6, 7, 8, 9}
>>> a={1,2}
>>> b={1,2,3,4}
>>> a<=b
True
>>> a>=b
False
>>> b>=a
True
>>> 2 in a
True
>>> 2 not in a
False
>>> a.issubset(b)
True
>>> a.issuperset(b)
False
>>> b.superset(a)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    b.superset(a)
AttributeError: 'set' object has no attribute 'superset'
>>> b.issuperset(b)
True
>>> b.issuperset(a)
True
>>> a.isdisjoint(b)
False
>>> a.add(3,4)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.add(3,4)
TypeError: add() takes exactly one argument (2 given)
>>> a.add(3)
>>> a
{1, 2, 3}
>>> a.update([10,20])
>>> a
{1, 2, 3, 10, 20}
>>> a.remove(10)
>>> a
{1, 2, 3, 20}
>>> a.pop()
1
>>> a
{2, 3, 20}
>>> a.clear()
>>> a
set()
>>> a={1, 2, 3, 4, 5, 6}
>>> a
{1, 2, 3, 4, 5, 6}
>>> a.copy()
{1, 2, 3, 4, 5, 6}
>>> #set methods
>>> max()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    max()
TypeError: max expected 1 arguments, got 0
>>> max(a)
6
>>> min(a)
1
>>> b=a
>>> a
{1, 2, 3, 4, 5, 6}
>>> b
{1, 2, 3, 4, 5, 6}
>>> b.copy(a)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    b.copy(a)
TypeError: copy() takes no arguments (1 given)
>>> a=b.copy()
>>> a
{1, 2, 3, 4, 5, 6}
>>> b
{1, 2, 3, 4, 5, 6}
>>> b.add(12)
>>> b
{1, 2, 3, 4, 5, 6, 12}
>>> a
{1, 2, 3, 4, 5, 6}
>>> c=a.copy()
>>> c
{1, 2, 3, 4, 5, 6}
>>> a
{1, 2, 3, 4, 5, 6}
>>> c.add(12)
>>> c
{1, 2, 3, 4, 5, 6, 12}
>>> c.add(13)
>>> c
{1, 2, 3, 4, 5, 6, 12, 13}
>>> a
{1, 2, 3, 4, 5, 6}
>>> sum(a)
21
>>> len(a)
6
>>> sorted(a)
[1, 2, 3, 4, 5, 6]
>>> a.pop()
1
>>> a.update({4,56,78})
>>> a
{2, 3, 4, 5, 6, 78, 56}
>>> a.remove(56)
>>> a
{2, 3, 4, 5, 6, 78}
>>> a.remove(56)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.remove(56)
KeyError: 56
>>> a.discard(56)
>>> a
{2, 3, 4, 5, 6, 78}
>>> all(a)
True
>>> a.add(0)
>>> all(a)
False
>>> a.any()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.any()
AttributeError: 'set' object has no attribute 'any'
>>> any(a)
True
>>> a=frozenset({1,12,13,10,18,59,20})
>>> a
frozenset({1, 18, 20, 10, 59, 12, 13})
>>> a.add(12)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
>>> d={}
>>> type(d)
<class 'dict'>
>>> d=dict()
>>> d={"k1":"v1","k2":"v2","k3":"v3"}
>>> d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
>>> id(d)
1601910487064
>>> d["k4"]="v4"
>>> d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
>>> d={]
SyntaxError: invalid syntax
>>> d={}
>>> d[1]='int'
>>> d[2.1]='float'
>>> d[3+7j]='bool'
>>> d["s"]="deepu"
>>> d((1,2,3))="tuple"
SyntaxError: can't assign to function call
>>> d=[(1,2,3)]="tuple"
SyntaxError: can't assign to literal
>>> SyntaxError: can't assign to literal
SyntaxError: EOL while scanning string literal
>>> d[(1,2,3)]="tuple"
>>> d
{1: 'int', 2.1: 'float', (3+7j): 'bool', 's': 'deepu', (1, 2, 3): 'tuple'}
>>> d[false]="false"
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    d[false]="false"
NameError: name 'false' is not defined
>>> d[(false)]='False'
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    d[(false)]='False'
NameError: name 'false' is not defined
>>> d(frozenset({1,2,4})="fset"
  d
  
SyntaxError: invalid syntax
>>> d
{1: 'int', 2.1: 'float', (3+7j): 'bool', 's': 'deepu', (1, 2, 3): 'tuple'}
>>> d[False]="bool"
>>> d
{1: 'int', 2.1: 'float', (3+7j): 'bool', 's': 'deepu', (1, 2, 3): 'tuple', False: 'bool'}
>>> d={}
>>> d[1]=1
>>> d[2]=12.4
>>> d[3]=12+4j
>>> d[4]='str'
>>> d[5]=[1,2,34]
>>> d[6]=(2,3,4)
>>> d[7]={1,2,3,4}
>>> d[8]={1:1}
>>> d[9]=True
>>> d
{1: 1, 2: 12.4, 3: (12+4j), 4: 'str', 5: [1, 2, 34], 6: (2, 3, 4), 7: {1, 2, 3, 4}, 8: {1: 1}, 9: True}
>>> 9 in d
True
>>> 10 n d
SyntaxError: invalid syntax
>>> 10 in d
False
>>> str in d
False
>>> d[5]
[1, 2, 34]
>>> d[8]
{1: 1}
>>> d[10]
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    d[10]
KeyError: 10
>>> d.get(10)
>>> d.get(1)
1
>>> # get will handle the error
>>> d.get(10,"key is not present")
'key is not present'
>>> d.get(6,"key is not present")
(2, 3, 4)
>>> d
{1: 1, 2: 12.4, 3: (12+4j), 4: 'str', 5: [1, 2, 34], 6: (2, 3, 4), 7: {1, 2, 3, 4}, 8: {1: 1}, 9: True}
>>> d[3]=4
>>> d
{1: 1, 2: 12.4, 3: 4, 4: 'str', 5: [1, 2, 34], 6: (2, 3, 4), 7: {1, 2, 3, 4}, 8: {1: 1}, 9: True}
>>> d[5]=10
>>> d
{1: 1, 2: 12.4, 3: 4, 4: 'str', 5: 10, 6: (2, 3, 4), 7: {1, 2, 3, 4}, 8: {1: 1}, 9: True}
>>> d[6]=12
>>> d
{1: 1, 2: 12.4, 3: 4, 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3, 4}, 8: {1: 1}, 9: True}
>>> d[7]=20
>>> d
{1: 1, 2: 12.4, 3: 4, 4: 'str', 5: 10, 6: 12, 7: 20, 8: {1: 1}, 9: True}
>>> d={}
>>> d
{}
>>> d={1: 1, 2: 12.4, 3: 4, 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3, 4}, 8: {1: 1}, 9: True}
>>> d
{1: 1, 2: 12.4, 3: 4, 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3, 4}, 8: {1: 1}, 9: True}
>>> 