Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list is an ordered,mutable collection,used to store multiple values in a single variable.
>>> #properties of list ordered,mutable,can store hetrogenious type data.
>>> l=[]
>>> l=list()
>>> l=[2,3,45,"python",[7,6,78],(34,8,90)]
>>> l
[2, 3, 45, 'python', [7, 6, 78], (34, 8, 90)]
>>> l*4
[2, 3, 45, 'python', [7, 6, 78], (34, 8, 90), 2, 3, 45, 'python', [7, 6, 78], (34, 8, 90), 2, 3, 45, 'python', [7, 6, 78], (34, 8, 90), 2, 3, 45, 'python', [7, 6, 78], (34, 8, 90)]
>>> l[1:4]
[3, 45, 'python']
>>> l[ : :-1]
[(34, 8, 90), [7, 6, 78], 'python', 45, 3, 2]
>>> i[0]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    i[0]
NameError: name 'i' is not defined
>>> l[0]
2
>>> l[10]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l[10]
IndexError: list index out of range
>>> 45 in l
True
>>> 45 not in l
False
>>> l.len()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l.len()
AttributeError: 'list' object has no attribute 'len'
>>> len(l)
6
>>> max(l)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> max("l")
'l'
>>> l.max()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l.max()
AttributeError: 'list' object has no attribute 'max'
>>> max(l)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> a=[23,56,1,89]
>>> maxx(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    maxx(a)
NameError: name 'maxx' is not defined
>>> max(a)
89
>>> min(a)
1
>>> sum(a)
169
>>> sorted(a)
[1, 23, 56, 89]
>>> list(a)
[23, 56, 1, 89]
>>> #list methods
>>> #adding elements
>>> a.append(56)
>>> a
[23, 56, 1, 89, 56]
>>> #append will add a value at the end of a list
>>> a.insert(1,67)
>>> a
[23, 67, 56, 1, 89, 56]
>>> #insert element at the specified index.
>>> #extend() is used a add mutliple values.
>>> a.extend(90,22,15)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.extend(90,22,15)
TypeError: extend() takes exactly one argument (3 given)
>>> a.extend(90)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.extend(90)
TypeError: 'int' object is not iterable
>>> a.extend([10,90,22,15])
>>> a
[23, 67, 56, 1, 89, 56, 10, 90, 22, 15]
>>> #Remove element methods.
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> a.remove(10)
>>> a
[23, 67, 56, 1, 89, 56, 90, 22, 15]
>>> a.pop(3)
1
>>> a
[23, 67, 56, 89, 56, 90, 22, 15]

>>> a.clear()
>>> a
[]
>>> a.extend([10,90,22,15])
>>> a
[10, 90, 22, 15]
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=[23, 67, 56, 1, 89, 56, 90, 22, 15]
>>> a
[23, 67, 56, 1, 89, 56, 90, 22, 15]
>>> #search methods , searching elements using index values.we have index(),count().
>>> a.index(5)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.index(5)
ValueError: 5 is not in list
>>> a.index(89)
4
>>> a.count(89)
1
>>> #sorting and reversing methods.
>>> a.sort()
>>> a
[1, 15, 22, 23, 56, 56, 67, 89, 90]
>>> a.reverse()
>>> a
[90, 89, 67, 56, 56, 23, 22, 15, 1]
>>> a.sorted()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.sorted()
AttributeError: 'list' object has no attribute 'sorted'
>>> #coping methods
>>> a.copy()
[90, 89, 67, 56, 56, 23, 22, 15, 1]
>>> #nested list
>>> data=[[12,34],[23,45]]
>>> data
[[12, 34], [23, 45]]
>>> data[0]
[12, 34]
>>> 
