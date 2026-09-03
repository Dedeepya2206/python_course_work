#polymorphism : Polymorphism means "Many Forms".
#In programming, polymorphism allows the same method, function, or operator to behave differently depending on the object, arguments, or data it is working with.
#This makes programs more flexible, reusable, and easier to extend.

#Python mainly supports the following types of polymorphism.
#1. Method Overloading (Compile-Time Polymorphism)
#2. Method Overriding (Run-Time Polymorphism)
#3. Operator Overloading

#Methodoverriding - same method,same parameters but different classes.
#Step-by-Step Logic:--
#1.Parent class defines a method → acts as a general/default behavior.
#2.Child class redefines the same method → provides specialized behavior.
#3.At runtime, when you call the method using a child object, Python looks for the method in the child class first.

#4.If found, the child’s method overrides the parent’s method.
#5.If not found, Python falls back to the parent’s method.

class Hotstar:

    def __init__(self, name):
        self.name = name
        print(f"Dear {self.name}, Welcome to the Hotstar!!")

    def login(self):
        print("You can login to the Hotstar!!")

    def dashboard(self):
        print("You can see the dashboard")

    def searchbar(self):
        print("You can search")

    def playcontrollers(self):
        print("Pause / Resume / Play")

    def history(self):
        print("You can see the recent videos")

    def ads(self):
        print("Ads will run")

    def quality(self):
        print("Quality is low")

    def access(self):
        print("You have limited access")

    def download(self):
        print("You cannot download high qaulity videos")

class PremiumHotstar(Hotstar):

    def __init__(self, name):
        self.name = name
        print(f"Dear {self.name}, Welcome to the Hotstar!!")

    def ads(self):
        print("Ads will not run")

    def quality(self):
        print("Quality is High")

    def access(self):
        print("You have unlimited access")

    def download(self):
        print("You can download high qaulity videos")



a = Hotstar("Bharat Dasari")
a.login()
a.dashboard()
a.searchbar()
a.playcontrollers()
a.history()
a.ads()
a.quality()
a.access()
a.download()


b = PremiumHotstar("Avinash")
b.login()
b.dashboard()
b.searchbar()
b.playcontrollers()
b.history()
b.ads()
b.quality()
b.access()
b.download()