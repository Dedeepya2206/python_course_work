#using object -> we can access instance method, class method, static method, classattribute, insattribute
 #using class-> we can acess  class method, static method, classattribute

class flipkart:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
   
        print(f"Hello {self.name}, Welcome to flipkart")

Dedeepya = flipkart("Dedeepya",8325435670)
Pallavi = flipkart("Pallavi",83345695670)
Naimisha = flipkart("Naimisha",8329860923)



 

