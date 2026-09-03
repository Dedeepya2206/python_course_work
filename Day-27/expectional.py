'''
k={1:12,12:13}
print(k[14])
l=[12,34]
print(l[10])
print(a)
print('1'+1)
print(10/0)

try:
    #a=int(input())
    k={1:12,2:13}
    #print(k[14])
    l=[232,54]
    #print(l[10])
    #print(10/0)
    #print('1'+1)

except ValueError:
    print("enter the correct datatype")
except KeyError:
    print("key not found")
except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("can't divide by 0")
except TypeError:
    print("enter the correct datatype")
except NameError:
    print("enter the correct datatype")

else:
    print("error free program")
finally:
    print("End of the program")

try:
    #a=int(input())
    k={1:12,12:13}
    #print(k[14])
    l=[232,54]
    #print(1[10])
    #print(10/0)
    #print('1'+1)
except (ValueError,NameError,KeyError,IndexError,ZeroDivisionError,TypeError)as e:
    print("Error Occured :",e)
else:
    print("Error free program")
finally:
    print("End of the program")

try:
    #a=int(input())
    k={1:12,12:13}
    #print(k[14])
    l=[232,54]
    #print(1[10])
    #print(10/0)
    #print('1'+1)
except Exception as e:
    print("Error Occured :",e)
else:
    print("Error free program")
finally:
    print("End of the program")
'''
try:
    amount=int(input("enter the amount : "))
    balance=5000
    if balance <0:
        raise Exception("Amount need to be positive")
except Exception as e:
    print("Error Occured :",e)
else:
    print("Error free program")
finally:
    print("End of the program")
