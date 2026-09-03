'''
#system modules sys.argv List of command-line arguments
sys.exit() Exits the program
sys.path List of paths for module search
sys.version Returns the Python version
import sys
print(sys.path)#to print the list of python files

import sys 
print(sys.version)# It give version of python

import sys
print("start")
sys.exit()
print("stop")

----------------------------------------------------------------
' #Platform modules.                                            '
' #platform.system() Returns OS name (e.g., Windows, Linux)     '
' #platform.release() OS release version                        '
' #platform.processor() Returns processor type                  '
---------------------------------------------------------------

import platform
print(platform.system())
print(platform.release())
print(platform.processor())

------------------------------------------------------------------
'''
#Mathematics module
'''
--------------------------------------------------------
' math.sqrt(x) Returns the square root of x            '
' math.pow(x, y) x raised to the power y (x^y)         '
' math.ceil(x) Smallest integer ≥ x                    '
' math.floor(x) Largest integer ≤ x                    '
' math.fabs(x) Absolute value of x                     '
' math.factorial(x) Factorial of x (x!)                '        
' math.gcd(x, y) Greatest common divisor               '   
' math.log(x, base) Logarithm of x to the given base   '
' math.sin(x) Sine of x (x in radians)                 '
' math.cos(x) Cosine of x                              '
' math.tan(x) Tangent of x                             ' 
' math.degrees(x) Convert radians to degrees           '
' math.radians(x) Convert degrees to radians           '
--------------------------------------------------------
'''
'''
math.pi π = 3.14159...
math.e Euler’s number ≈ 2.718

import math
print(math.pi)
print(math.e)
print(math.sqrt(36))
print(math.pow(2,3))

import math
#ceil is for upper value. we get larger value
print(math.ceil(12.0001))
print(math.ceil(12.3201))
print(math.ceil(12.671))
print(math.ceil(13.56))
#floor for smaller interger.we get lower value
print(math.floor(12.0001))
print(math.floor(12.3201))
print(math.floor(12.671))
print(math.floor(13.9601))

import math
print(math.fabs(-10))
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(90))
print(math.degrees(30))
print(math.radians(30))
'''

