Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers = (10, 20, 30)
>>> names = ("Ravi", "Teja", "Ankit")
>>> mixed = (10, "Python", 5.5, True)
>>> numbers
(10, 20, 30)
>>> names
('Ravi', 'Teja', 'Ankit')
>>> mixed
(10, 'Python', 5.5, True)
>>> t()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t()
NameError: name 't' is not defined
>>> t=()
>>> t=(10,)
>>> t
(10,)
>>> a=(1,2)
>>> b=(6,7)
>>> a+b
(1, 2, 6, 7)
>>> a*4
(1, 2, 1, 2, 1, 2, 1, 2)
>>> numbers([0])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    numbers([0])
TypeError: 'tuple' object is not callable
>>> numbers[3]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    numbers[3]
IndexError: tuple index out of range
>>> numbers[2]
30
>>> numbers[-1]
30
>>> numbers[1:3]
(20, 30)
>>> names[1:2]
('Teja',)
>>> 'Teja' in names
True
>>> 'Teja',not in names
SyntaxError: invalid syntax
>>> 'Teja' not in names
False
>>> len(numbers)
3
>>> max(numbers)
30
>>> min(numbers)
10
>>> sum(10,20,30)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    sum(10,20,30)
TypeError: sum expected at most 2 arguments, got 3
>>> sum((10,12,15))
37
>>> sorted(numbers)
[10, 20, 30]
>>> tuple("names")
('n', 'a', 'm', 'e', 's')
>>> tuple(names)
('Ravi', 'Teja', 'Ankit')
>>> any((o,o,1))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    any((o,o,1))
NameError: name 'o' is not defined
>>> any((0,0,1))
True
>>> all((1,2,3))
True
>>> any((names))
True
>>> count(numbers)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    count(numbers)
NameError: name 'count' is not defined
>>> names.count()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    names.count()
TypeError: count() takes exactly one argument (0 given)
>>> numbers.count()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    numbers.count()
TypeError: count() takes exactly one argument (0 given)
>>> numbers.count(30)
1
>>> numbers.index(30)
2
>>> d=10,30,67
>>> d
(10, 30, 67)
>>> d=10,20,30
>>> d
(10, 20, 30)
>>> a,b,c=d
>>> a
10
>>> b
20
>>> c
30
>>> d=((1,2),(3,4))
>>> print(d[0])
(1, 2)
>>> print(d[1][1])
4
>>> d=(10,20,30)
>>> data[0]=100
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    data[0]=100
NameError: name 'data' is not defined
>>> d=(10,20,30,[1,2,3],40)
>>> d[3].append(60)
>>> d
(10, 20, 30, [1, 2, 3, 60], 40)
>>> 