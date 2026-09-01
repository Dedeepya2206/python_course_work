#single Inheritance
'''
class WhatsappV1:
    def messaging(self):
        print("You can Message")

class WhatsappV2(WhatsappV1):
    def calls(self):
        print("you can audio and video calls")

a = WhatsappV1()
a.messaging()

b = WhatsappV2()
b.calls()

#Multi-level Inheritance

class WhatsappV1:
    def messaging(self):
        print("You can Message")

class WhatsappV2(WhatsappV1):
    def calls(self):
        print("you can audio and video calls")

class whatsappV3(WhatsappV2):
    def status(self):
        print("You can add the status for 24 hrs")


a = WhatsappV1()
a.messaging()

b = WhatsappV2()
b.messaging()
b.calls()

c = whatsappV3()
c.messaging()
c.calls()
c.status()

#Multiple Inheritance - Multiple parents,single childs

class WhatsappV1:
    def messaging(self):
        print("You can Message")


class WhatsappV2:
    def calls(self):
        print("You can audio and video calls")


class WhatsappV3(WhatsappV1, WhatsappV2):
    def status(self):
        print("You can add the status for 24 hrs")


# Whatsapp V1 object
a = WhatsappV1()
a.messaging()

# Whatsapp V2 object
b = WhatsappV2()
b.calls()

# Whatsapp V3 object
c = WhatsappV3()
c.messaging()
c.calls()
c.status()


#Hierarchy Inheritance - single parent,multiple childs

class WhatsappV1:
    def messaging(self):
        print("You can Message")


class WhatsappV2(WhatsappV1):
    def calls(self):
        print("You can audio and video calls")


class WhatsappV3(WhatsappV1):
    def status(self):
        print("You can add the status for 24 hrs")


# Whatsapp V1 object
a = WhatsappV1()
a.messaging()

# Whatsapp V2 object
b = WhatsappV2()
b.messaging()
b.calls()

# Whatsapp V3 object
c = WhatsappV3()
c.messaging()
c.status()


# Hybride Inheritance - it's the combination of any to inheritances

class WhatsappV1:
    def messaging(self):
        print("You can Message")


class WhatsappV2:
    def extramessage(self):
        print("You can add emojis, stickers, gifs")

class whatsappV3(WhatsappV1,WhatsappV2):
    def calls(self):
        print("You can audio and video calls")


class WhatsappV4(whatsappV3):
    def status(self):
        print("You can add the status for 24 hrs")


# Whatsapp V1 object
a = WhatsappV1()
a.messaging()

# Whatsapp V2 object
b = WhatsappV2()
b.extramessage()

# Whatsapp V3 object
c = whatsappV3()
c.messaging()
c.extramessage()
c.calls()

d = WhatsappV4()
d.messaging()
d.extramessage()
d.calls()

#super() - whenever their is same methods we use super keyword to access the parents class method

class WhatsappV1:
    def status(self):
        print("you can add images and videos")

class WhatsappV2(WhatsappV1):
    def status(self):
        super().status()
        print("You can add music and strickers")

class WhatsappV3(WhatsappV2):
    def status(self):
        super().status()
        print("You can likre and you can add reaction")

a = WhatsappV3()
a.status()
'''
# In mutiple inheritance to access the parent class method we use classname and self for acquring the properties of parent class

class whatsappv1:
    def status(self):
        print("you can add images and videos")
        
class whatsappv2:
    def status(self):
        print("You can add music and stickers")

class whatsappv3(whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can like and you can add reaction")


a=whatsappv3()
a.status()