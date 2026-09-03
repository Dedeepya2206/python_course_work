
units=int(input("enter the value :"))
senior=input("enter the vaule : ").lower()=="true"
if 0<=units<=100:
    bill=units*1.5
    
elif 101<=units<=200:
    bill =units*2.5
    
elif 201<=units<=500:
    bill=units*4
    
elif 500<units<=800:
    bill=units*6
   
else:
    bill=unit*1.05*6
if senior:
    bill*=0.90
print(bill)
'''
units = int(input("enter a value : "))
s_c = eval(input("enter True or False : "))

if units > 0 and units <= 100:
    bill = units * 1.5

elif units >= 101 and units <= 200:
    bill = units * 2.5

elif units >= 201 and units <= 500:
    bill = units * 4

elif units > 500:
    bill = units * 6

if s_c == True:
    bill = bill - (bill * 0.10)

if units > 800:
    bill = bill + (bill * 0.05)

print(bill)
'''