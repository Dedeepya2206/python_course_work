class Instagram:
    #variable are decalred isndie the function
    def __init__(self,username,password,post):
        self.username = username
        self.__passowrd= password #private
        self._post= [] #protected--->getter,setter


#getpassword or xyz --->is just a word 
    def getpassword(self):
        return self.__passowrd

    def setpassword(self,newpassword):
        self.__passowrd = newpassword
    

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)


    
    def display(self):
        print(self.username,self.__passowrd,self._post)


#object create chesukuntunam
Dedeepya = Instagram('Dedeepya','Dedeepya@123',3)
Dedeepya.display() #object.display()
print(Dedeepya.username)
print(Dedeepya.getpassword())
print(Dedeepya.accesspost)


Dedeepya.username='Dedeepya'
Dedeepya.setpassword('Dedeepya@123')
Dedeepya.accesspost="sunrise.png"
Dedeepya.accesspost="beach.png"
Dedeepya.accesspost="forest.png"

print(Dedeepya.username)
print(Dedeepya.getpassword())
print(Dedeepya.accesspost)