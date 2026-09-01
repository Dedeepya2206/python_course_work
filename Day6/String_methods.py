Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #strings.
>>> #funtion in str are len(),min/max(),sorted(),chr()/ord().
>>> c='Dedeepya'
>>> len(c)
8
>>> ord("e")
101
>>> ord("a")
97
>>> ord(0)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ord(0)
TypeError: ord() expected string of length 1, but int found
>>> ord("o")
111
>>> chr(65)
'A'
>>> chr(66)
'B'
>>> chr(60)
'<'
>>> min(c)
'D'
>>> max(c)
'y'
>>> sorted(c)
['D', 'a', 'd', 'e', 'e', 'e', 'p', 'y']
>>> #case methods
>>> c='String is immutable'
>>> c.upper()
'STRING IS IMMUTABLE'
>>> c.lower()
'string is immutable'
>>> c.capitalize()
'String is immutable'
>>> c.title()
'String Is Immutable'
>>> c.swapcase()
'sTRING IS IMMUTABLE'
>>> "STRAẞEMÁLAGAÅngströmCaf
é".casefold()
SyntaxError: EOL while scanning string literal
>>> "STRAẞEMÁLAGAÅngströmCafé".casefold()
'strassemálagaångströmcafé'
>>> #Python Methods.
>>> c
'String is immutable'
>>> c.center(60,'-')
'--------------------String is immutable---------------------'
>>> c.center(60,'*')
'********************String is immutable*********************'
>>> c.center(60,'0')
'00000000000000000000String is immutable000000000000000000000'
>>> c.ljust(60,'-')
'String is immutable-----------------------------------------'
>>> c.rjust(60,'-')
'-----------------------------------------String is immutable'
>>> '12'.zfill(4)
'0012'
>>> '12'.zfill(4)
'0012'
>>> '12'.zfill(14)
'00000000000012'
>>> '3456'.zfill(6)
'003456'
>>> #search and find methods
>>> c
'String is immutable'
>>> c.find('S')
0
>>> c.find('i')
3
>>> c.find('z')
-1
>>> c.rfind('m')#we will get from right side first occurance
12
>>> c.rfind('i')
10
>>> c.index('i')
3
>>> c.rindex('i')
10
>>> c.index('z')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    c.index('z')
ValueError: substring not found
>>> c
'String is immutable'
>>> c.count('i')
3
>>> c.count('g')
1
>>> c.count('m')
2
>>> #string Testing Method(Boolen results): startswith,endswith,isalnum,islower,isupper,isspace,istitle,isidentifier.
>>> c
'String is immutable'
>>> c.startswith('St')
True
>>> c.endswith('ble')
True
>>> c.endswith(''cc'')
SyntaxError: invalid syntax
>>> c.endswith('cc')
False
>>> #replace and modify methods.
>>> c
'String is immutable'
>>> c.replace("i",'0')
'Str0ng 0s 0mmutable'
>>> c.replace("String","Float")
'Float is immutable'
>>> c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
>>> c.translate(c.maketrans('aeiou','12345'))
'Str3ng 3s 3mm5t1bl2'
>>> c.translate(c.maketrans('aeiou','*****'))
'Str*ng *s *mm*t*bl*'
>>> c.translate(c.maketrans('aeiou','12**5'))
'Str*ng *s *mm5t1bl2'
>>> #Splitting & Joining Methods
>>> c.split()
['String', 'is', 'immutable']
>>> c
'String is immutable'
>>> 'String,is,immutable'.split()
['String,is,immutable']
>>> 'String,is,immutable'.split(,)
SyntaxError: invalid syntax
>>> 'String,is,immutable'.split(',')
['String', 'is', 'immutable']
>>> 'String,is,immutable'.rsplit()
['String,is,immutable']
>>> 'String,is,immutable'.split(' ',)
['String,is,immutable']
>>> 'String,is,immutable'.split(' ', 1)
['String,is,immutable']
>>> 'String,is,immutable'.rsplit()
['String,is,immutable']
>>> 'String,is,immutable'.rsplit(' ', 1)
['String,is,immutable']
>>> 'String,is,immutable'.split( ' ',1)
['String,is,immutable']
>>> c.splitlines()
['String is immutable']
>>> ' '.join([' ', 'Python', 'programming', 'lang])
	  
SyntaxError: EOL while scanning string literal
>>> ' '.join([' ', 'Python', 'programming', 'lang'])
'  Python programming lang'
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> s='java, python,c,c++'
>>> s.partition('.')
('java, python,c,c++', '', '')
>>> s.partition(',')
('java', ',', ' python,c,c++')
>>> s.rpartition(',')
('java, python,c', ',', 'c++')
>>> s.lpartition(',')
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    s.lpartition(',')
AttributeError: 'str' object has no attribute 'lpartition'
>>> '_ '.join([' ', 'Python', 'programming', 'lang'])
' _ Python_ programming_ lang'
>>> ' /'.join([' ', 'Python', 'programming', 'lang'])
'  /Python /programming /lang'
>>> #Whitespace & Trimming Methods
>>> c
'String is immutable'
>>> c.strip()
'String is immutable'
>>> c.lstrip()
'String is immutable'
>>> ---"Hello".lstrip()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    ---"Hello".lstrip()
TypeError: bad operand type for unary -: 'str'
>>> ---"hello".lstrip("-")
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    ---"hello".lstrip("-")
TypeError: bad operand type for unary -: 'str'
>>> "---hello".lstrip("-")
'hello'
>>> "hello----".rstrip("-")
'hello'
>>> c='     hello     world'
>>> c.strip()
'hello     world'
>>> c.lstrip()
'hello     world'
>>> c.rstrip()
'     hello     world'
>>> #Encoding & Decoding Methods
>>> c.encode("utf-8")
b'     hello     world'
>>> c.decode("utf-8")
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    c.decode("utf-8")
AttributeError: 'str' object has no attribute 'decode'
>>> c.decode()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    c.decode()
AttributeError: 'str' object has no attribute 'decode'
>>> text = "Hello नमस्ते你好 café 🙂">>
SyntaxError: invalid syntax
>>> text = "Hello 🙂"
>>> text.encode()
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode
<built-in method decode of bytes object at 0x000001EC92097AB0>
>>> b'Hello \xf0\x9f\x99\x82'decode()
SyntaxError: invalid syntax
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'
>>> 