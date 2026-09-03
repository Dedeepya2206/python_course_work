Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #print stmt
>>>  print('a=%d b=%.2f c=%s'%(a,b,c))
 
SyntaxError: unexpected indent
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print('a=%d b=%.2f c=%s'%(a,b,c))
NameError: name 'a' is not defined
>>> a=20
>>> b=30.98
>>> c="Deepu"
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=20 b=30.98 c=Deepu
>>> print("a ={}| b = {}| c = {}".format(a,b,c))
a =20| b = 30.98| c = Deepu
>>> print("a ={}| b = {}| c = {}".format(c,a,b))
a =Deepu| b = 20| c = 30.98
>>> print("a ={1}| b = {2}| c = {0}".format(a,b,c))
a =30.98| b = Deepu| c = 20
>>> 