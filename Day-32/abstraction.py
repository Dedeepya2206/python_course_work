from abc import ABC,abstractmethod
class phonepay(ABC):
    def senderinfo(self):
        print("You can emter mobile number or scanner")
    def amount(self):
        print("You can enter amount")
    def pin(self):
        print("you need to enter the pin")

    @abstractmethod
    def transaction(self):
        pass


class HDFC(phonepay):
    def transaction(self):
        print("Payment using HDFC bank")

class SBI(phonepay):
    def transaction(self):
        print("Payment using SBI bank")

class BOB(phonepay):
    def transaction(self):
        print("Payment using BOB bank")

class Union(phonepay):
    def transaction(self):
        print("Payment using Union bank")

class CGB(phonepay):
    def transaction(self):
        print("Payment using CGB bank")

Dedeepya=HDFC()
Dedeepya.senderinfo()
Dedeepya.amount()
Dedeepya.pin()
Dedeepya.transaction()

Pallavi=SBI()
Pallavi.senderinfo()
Pallavi.amount()
Pallavi.pin()
Pallavi.transaction()

Naimisha=BOB()
Naimisha.senderinfo()
Naimisha.amount()
Naimisha.pin()
Naimisha.transaction()

Likitha=Union()
Likitha.senderinfo()
Likitha.amount()
Likitha.pin()
Likitha.transaction()

Chandra=CGB()
Chandra.senderinfo()
Chandra.amount()
Chandra.pin()
Chandra.transaction()