class flipkart:
    products={"Shirts":1000,"Handbag":2000,"Pants":3000}
    discount = 30

    @classmethod
    def display(cls):
        print(cls.products)


    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello {self.name}, Welcome to flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{flipkart.discount}% discount is going on, grab the product....")

Dedeepya = flipkart()
Dedeepya.userinfo("Dedeepya",9876543210,"Rcl")
Dedeepya.displaydiscount()
Dedeepya.display()

Pallavi = flipkart()
Pallavi.userinfo("Pallavi",976845320,"TG")
Pallavi.displaydiscount()
Pallavi.display()

Naimisha = flipkart()
Naimisha.userinfo("Naimisha",9845643203,"Vij")
Naimisha.displaydiscount()
Naimisha.display()