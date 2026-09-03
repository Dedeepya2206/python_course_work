Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #strings:Collection of characters,it is a immutable,enclosed with a"",''.
>>> s=''
>>> s
''
>>> s='deepu'
>>> s
'deepu'
>>> #concatination
>>> s="Dedeepya"
>>> c="PFS"
>>> s+c
'DedeepyaPFS'
>>> #repeation
>>> 'Dedeepya'*10
'DedeepyaDedeepyaDedeepyaDedeepyaDedeepyaDedeepyaDedeepyaDedeepyaDedeepyaDedeepya'
>>> #indexing: accessing a particular specific value using a index
>>> s="Dedeepya"
>>> s(4)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s(4)
TypeError: 'str' object is not callable
>>> s[4]
'e'
>>> s[1]
'e'
>>> s[8]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s[8]
IndexError: string index out of range
>>> s[6]
'y'
>>> s[3]
'e'
>>> names='Deepu pallavi harsha nisha'
>>> names[0]
'D'
>>> name[4]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    name[4]
NameError: name 'name' is not defined
>>> name[-1]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    name[-1]
NameError: name 'name' is not defined
>>> names[-1]
'a'
>>> #syntax for slicing s[start:end+1:step]
>>> #s[0:len:1]
>>> names[0:5]
'Deepu'
>>> names[:5]
'Deepu'
>>> names[7:12]
'allav'
>>> names[3:21]
'pu pallavi harsha '
>>> names[-1:-8]
''
>>> names[-1:-7]
''
>>> names[-1:-8:-1]]
SyntaxError: invalid syntax
>>> names[-1:-8:-1]
'ahsin a'
>>> name[::-1]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    name[::-1]
NameError: name 'name' is not defined
>>> names[::-1]
'ahsin ahsrah ivallap upeeD'
>>> names[:2:]
'De'
>>> names[::2]
'Deuplaihrh ih'
>>> Deepu in names
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    Deepu in names
NameError: name 'Deepu' is not defined
>>> 'Deepu' in names
True
>>> 'Deepu' not in names
False
>>> #Bulitin functions
>>> #len()
>>> print(len(names))
26
>>> print(max(names))
v
>>> print(min(names))
 
>>> print(sorted("Deepu"))
['D', 'e', 'e', 'p', 'u']
>>> print(ord['A'])
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(ord['A'])
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(chr[65])
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(chr[65])
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(chr(65))
A
>>> print(ord('A'))
65
>>> print("deepu".upper())
DEEPU
>>> print('deepu'.lower())
deepu
>>> names.capitalize()
'Deepu pallavi harsha nisha'
>>> names.title()
'Deepu Pallavi Harsha Nisha'
>>> print('Hi'.center(6,'*')
      )
**Hi**
>>> names.find("n")
21
>>> names.count()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    names.count()
TypeError: count() takes at least 1 argument (0 given)
>>> count(names)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    count(names)
NameError: name 'count' is not defined
>>> names.count(s)
0
>>> names.startswith("Python")
False
>>> names.endswith("nisha")
True
>>> names.replace("a","b")
'Deepu pbllbvi hbrshb nishb'
>>> names.split()
['Deepu', 'pallavi', 'harsha', 'nisha']
>>> print(join('-'.join([names])))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(join('-'.join([names])))
NameError: name 'join' is not defined
>>> 