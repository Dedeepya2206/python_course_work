Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,45,7]
>>> l
[1, 2, 3, 45, 7]
>>> l.append(12)
>>> l.append(14)
>>> l
[1, 2, 3, 45, 7, 12, 14]
>>> l.insert(1,13)
>>> l
[1, 13, 2, 3, 45, 7, 12, 14]
>>> l.extend([20,25,67])
>>> l
[1, 13, 2, 3, 45, 7, 12, 14, 20, 25, 67]
>>> l[3]=60
>>> l
[1, 13, 2, 60, 45, 7, 12, 14, 20, 25, 67]
>>> 1[5]=70
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    1[5]=70
TypeError: 'int' object does not support item assignment
>>> l[4]=90
>>> l
[1, 13, 2, 60, 90, 7, 12, 14, 20, 25, 67]
>>> l.pop()
67
>>> l.pop()
25
>>> l
[1, 13, 2, 60, 90, 7, 12, 14, 20]
>>> l[5]=80
>>> l
[1, 13, 2, 60, 90, 80, 12, 14, 20]
>>> l.pop(1)
13
>>> l
[1, 2, 60, 90, 80, 12, 14, 20]
>>> l.pop(4)
80
>>> l
[1, 2, 60, 90, 12, 14, 20]
>>> l.remove(14)
>>> l
[1, 2, 60, 90, 12, 20]
>>> del l[1]
>>> l
[1, 60, 90, 12, 20]
>>> l.clear()
>>> l
[]
>>> id(l)
2455263781192
>>> l=[1,23,4,567,89,90]
>>> max(l)
567
>>> min(l)
1
>>> sorted(l)
[1, 4, 23, 89, 90, 567]
>>> l.reverse()
>>> l
[90, 89, 567, 4, 23, 1]
>>> l.sort()
>>> l
[1, 4, 23, 89, 90, 567]
>>> l.sort(reverse=True)
>>> l
[567, 90, 89, 23, 4, 1]
>>> sum(l)
774
>>> n=[1,2,3]
>>> m=[1,2,3]
>>> n
[1, 2, 3]
>>> m
[1, 2, 3]
>>> x=n
>>> n
[1, 2, 3]
>>> n.append(12)
>>> n
[1, 2, 3, 12]
>>> x
[1, 2, 3, 12]
>>> m=l.copy()
>>> m
[567, 90, 89, 23, 4, 1]
>>> 
>>> m=l.copy()
>>> m
[567, 90, 89, 23, 4, 1]
>>> l
[567, 90, 89, 23, 4, 1]
>>> all([0,"",[],(),{},False])
False
>>> all([1],0,"",(),{})
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    all([1],0,"",(),{})
TypeError: all() takes exactly one argument (5 given)
>>> any([1,"",[],(),{},False])
True
>>> l.index(23)
3
>>> l.count(25)
0
>>> l
[567, 90, 89, 23, 4, 1]
>>> l=[[1,2,3],[2,3,4]]
>>> l[0]
[1, 2, 3]
>>> l[0][2]
3
>>> 1[0][1]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    1[0][1]
TypeError: 'int' object is not subscriptable
>>> l[0] [2]
3
>>> 1[1] [3]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    1[1] [3]
TypeError: 'int' object is not subscriptable
>>> l[1] [2]
4
>>> l[-1][-1]
4
>>> #Tuple
>>> t=()
>>> t=tuple()
>>> t=(1,2,3,4,5,6,7)
>>> s=(4,5,6,7,8,9)
>>> t+s
(1, 2, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8, 9)
>>> t*5
(1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7)
>>> 6 in t
True
>>> 2 in s
False
>>> t
(1, 2, 3, 4, 5, 6, 7)
>>> s
(4, 5, 6, 7, 8, 9)
>>> s[2]
6
>>> t[3]
4
>>> t[:2]
(1, 2)
>>> a=1,2,3
>>> a
(1, 2, 3)
>>> a,b,c,d,e=t
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a,b,c,d,e=t
ValueError: too many values to unpack (expected 5)
>>> a,b,c,d,e=b
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a,b,c,d,e=b
NameError: name 'b' is not defined
>>> a,b,c,d,e=t
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a,b,c,d,e=t
ValueError: too many values to unpack (expected 5)
>>> a,b,c,d,e,f,g=t
>>> a
1
>>> b
2
>>> c
3
>>> d
4
>>> e
5
>>> f
6
>>> g
7
>>> len(t)
7
>>> max(t)
7
>>> min(t)
1
>>> sorted(t)
[1, 2, 3, 4, 5, 6, 7]
>>> sum(t)
28
>>> t.index(6)
5
>>> t.index(7)
6
>>> t
(1, 2, 3, 4, 5, 6, 7)
>>> t.count(3)
1
>>> t=(() ())
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    t=(() ())
TypeError: 'tuple' object is not callable
>>> t=((1,2),(2,3),(7,8),(9,10))
>>> t[0]
(1, 2)
>>> t[-2]
(7, 8)
>>> t[-1][-1]
10
>>> t=(1,2,3,[4,5],6,True)
>>> t
(1, 2, 3, [4, 5], 6, True)
>>> t[1]=20
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    t[1]=20
TypeError: 'tuple' object does not support item assignment
>>> t[3]
[4, 5]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 10], 6, True)
>>> 