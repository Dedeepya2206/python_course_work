'''
def retrivedata():
    data=['1...100','101...200','201...300','301...400','401...500','501...600','601...700','701...800']
    for i in data:
        yield i
reels = retrivedata()
while True:
    status=input("[s]croll or [q]uit :")
    if status == 's':
        print(next(reels))
    else:
        break

#even number
def even():
    i=0
    while True:
        i+=2
        yield i
n=10
res=even()
for i in range(n):
    print(next(res))

#To find the factors
def factors(n):
    i = 1
    while i <= n:
        if n % i == 0:
            yield i
        i += 1

num = 10

for f in factors(num):
    print(f)

# To print fibnanoic series.
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
for num in fibonacci(10):
    print(num)


#To print Prime numbers.(Type-1)
def prime_numbers(n):
    num = 2
    while num <= n:
        i = 2
        is_prime = True
        
        while i <= num // 2:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        
        if is_prime:
            yield num
        
        num += 1


for p in prime_numbers(20):
    print(p)

#To print prime numbers upto n range.(Type-2)
def primes(n):
    num = 2
    while num <= n:
        i = 2
        while i < num:
            if num % i == 0:
                break
            i += 1
        else:
            yield num
        num += 1


for p in primes(10):
    print(p)

#To print prime.(Type 3)
def isprime(n):
    for j in range(2,n//2+1):
        if n%j==0:
            return False
    return True
def primes(n):
    for i in range(2,n+1):
        if isprime(i):
            yield i
n=50
res = primes(n)
for i in res:
    print(i)
'''
#To print countdown from 10 to 1 
def countdown():
    num = 10
    while num >= 1:
        yield num
        num -= 1

res = countdown()


print(next(res))
print(next(res))
print(next(res))
print(next(res))
