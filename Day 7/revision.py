Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[]
>>> l=list()
>>> l=[1,23.4,56,"str",[1,2,3],(5,7,8),{1,3,4,5},{1:,2:23,3:4}]
SyntaxError: invalid syntax
>>> l=[1,23.4,56,"str",[1,2,3],(5,7,8),{1,3,4,5},{1:1,2:23,3:4}]
>>> l
[1, 23.4, 56, 'str', [1, 2, 3], (5, 7, 8), {1, 3, 4, 5}, {1: 1, 2: 23, 3: 4}]
>>> type(l)
<class 'list'>
>>> l=[1,2,3,45]
>>> m=[5,6,7]
>>> l+m
[1, 2, 3, 45, 5, 6, 7]
>>> m*3
[5, 6, 7, 5, 6, 7, 5, 6, 7]
>>> l[3]
45
>>> l[1:]
[2, 3, 45]
>>> 1[::-1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    1[::-1]
TypeError: 'int' object is not subscriptable
>>> l[ : :-1]
[45, 3, 2, 1]
>>> 1[0:]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    1[0:]
TypeError: 'int' object is not subscriptable
>>> l[ : 3]
[1, 2, 3]
>>> 