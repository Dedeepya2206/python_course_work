Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> A=20
>>> a
10
>>> A
20
>>> a=10
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a=10
>>> b=20
>>> a,b=b,c
>>> a
20
>>> b
30
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 