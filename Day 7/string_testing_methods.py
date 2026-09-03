Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c='string.py'
>>> c.startwith('str')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    c.startwith('str')
AttributeError: 'str' object has no attribute 'startwith'
>>> c.isalpha()
False
>>> c.isalnum()
False
>>> 's1234'.isalnum()
True
>>> c.isupper()
False
>>> c.islower()
True
>>> '     '.isspace()
True
>>> c.isspace()
False
>>> c.istitle()
False
>>> c.isidentifier()
False
>>> False
False
>>> 'This Is Title'.istitle()
True
>>> 'my@Fee'.isidentifier()
False
>>> c.startswith('str')
True
>>> c.endswith('py')
True
>>> 