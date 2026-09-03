'''
1.a->b#single
2.a,b,c,d->e #multiple
3.a->b->c->multi level
4.a->b,c,d->hyr
5.+->hybrid
'''
class whatsappV1:
    def __init__(self,name):
        self.name = name
        print(f"Welcome to the whatsapp - V1 {self.name}!")
    def messaging(self):
        print("You can send message")

    
class whatsappV2(whatsappV1):
    def __init__(self,name):
        self.name = name
        print(f"Welcome to the whatsapp - V1 {self.name}!")
    def calls(self):
        print("You can audio and vedio calls")

Dedeepya = whatsappV1("Dedeepya")
Dedeepya.messaging()
Deepu = whatsappV2("Deepu")
Deepu.messaging()
Deepu.calls()
