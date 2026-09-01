'''
 - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -
' random.random() Returns a float in the range [0.0, 1.0)                   '
' random.randint(a, b) Returns random integer between a and b (inclusive)   '
' random.uniform(a, b) Returns a float between a and b                      '
' random.choice(seq) Returns a random element from a non-empty sequence     '
' random.choices(seq,k=n) Returns a list of k random elements from seq      '
' random.shuffle(list) Shuffles the list in place                           '
' random.seed(n) Sets the seed for reproducibility                          '
'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

import random
#if we use seed() we get same output random.seed(10)
print(random.randint(10,20))
print(random.randint(10000,90000))
print(random.random())
print(random.uniform(1,6))
l=["R","P","S"]
print(random.choice(l))
print(random.choices(l,k=2))
random.shuffle(l)
print(l)
#if we donot use seed we will gwt different output foe every execution.
'''
#collections
'''
- - - - - - - - - - - - - - - - - - - - - - - - - 
' #Counter Counts frequency of elements            '
' #defaultdict Dictionary with default values      '
' #deque Double-ended queue for fast appends/pops  '
- - - - - - - - - - - - -  - - - - - - - - - - - 
from  collections import Counter
s="Python Programming"
l=[1,1,1,1,2,3,4,5,445,12,34,56,78,89,78,4,5]
m="this is that that is this is".split()
print(Counter(s))
print(Counter(l))
print(Counter(m))

#for int float string
from  collections import Counter,defaultdict
s="Python Programming"
l=[1,1,1,1,2,3,4,5,445,12,34,56,78,89,78,4,5]
m="this is that that is this is".split()

d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)

d=defaultdict(float)
for i in s:
    d[i]+=1
print(d)

d=defaultdict(str)
for i in s:
    d[i]+='1'
print(d)

#deque
from collections import deque
l= deque ([])
l.appendleft(10)
l.append(20)
l.append(30)
l.popleft( )
l.popleft()
l.append(50)
l.append(70)
l.popleft()
l.appendleft(60)
l.pop()
print(l)
'''
#itertools
'''
from itertools import combinations, permutations
res1=list(combinations('abc',2))
res2=list(permutations('abc',2))
print(res1)
print(res2)
'''
from itertools import combinations, permutations
res1=list(combinations('abc',2))
res2=list(permutations('abc',2))
print([' '.join(i) for i in res1])
print([' '.join(i) for i in res2])