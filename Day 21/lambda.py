'''
greater = lambda a,b: a if a>b else b
print(greater(10,4))
print(greater(8,10))
print(greater(100,200))

wish=lambda name: f'welcome to course {name}'
print(wish("Deepu"))
print(wish("Pallavi"))
print(wish("Naimisha"))
print(wish("Harsha"))

iseven=lambda n: "Even" if n%2==0 else "Odd"
print(iseven(6))
print(iseven(105))
print(iseven(19))
print(iseven(10))

avg=lambda a,b,c: (a+b+c)/3
print(avg(10,20,30))
print(avg(120,270,60))
print(avg(100,210,330))


domain=lambda mail:(mail.split('@')[-1]).split(".")[0]
print(domain("dedeepya@gmail.com"))
print(domain("dedeepya@yahoo.com"))
print(domain("dedeepya@outlook.com"))


gst=lambda price: price +price*0.18
print(gst(1000))
print(gst(8000))
print(gst(5000))
print(gst(7000))

prices=[5000,1230.4560,7890]
res=list(map(lambda price:price+price*0.18,prices))
print(res)

names=["deepu","pallavi","naimisha","harsha"]
res=list(map(lambda name:name.title(),names))
print(res)

prices=[5000,1230.4560,7890]
res=list(map(lambda price:price-price*0.30,prices))
print(res)

names=("deepu","pallavi","naimisha","harsha")
res=tuple(map(lambda name:name.title(),names))
print(res)

names=("deepu","pallavi","naimisha","harsha")
res=set(map(lambda name:name.title(),names))
print(res)

prices=[5687,2345,6789,1020,6789]
res=list(filter(lambda prices: prices>5000,prices))
print(res)

prices=[5687,2345,6789,1020,6789]
res=list(filter(lambda prices: prices%2==0,prices))
print(res)

prices=[5687,2345,6789,1020,6789]
res=list(filter(lambda prices: prices%2!=0,prices))
print(res)

names={"Deepu","Pallavi","Naisha","Harsha","nandu","ajay","Tara"}
res=list(filter(lambda name: len(name)>5, names))
print(res)


#reduce function.
from functools import reduce
l=[3,56,789,786,654,546,234,453]
res=reduce(lambda sum,i:sum+i, l)
print(res)

# To combine all the things
from functools import reduce

names={"Deepu","Pallavi","Naisha","Harsha","nandu","ajay","Tara"}
res=reduce(lambda res,i: res+' '+i, names)
print(res)


products={'suagr':60,'salt':50,'eggs':30,'cooking oil':120,'bread':45}
print (dict(sorted(products.items( ))))
print (dict(sorted(products.items( ),reverse=True)))
print (dict(sorted(products.items(),key=lambda i:i[1])))
print (dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))
'''
