'''
#position arguments
def display(name,gmail,password):
    print(f"name: {name}")
    print(f"gmail: {gmail}")
    print(f"password: {password}")
display("Deepu","deepu@gmail.com","deepu@2215")
display("Deepu@2215","deepu","deepu@gmail.com")
display("Deepu@gmail.com","deepu@2215","deepu")

#keyword arguments
def display(name,gmail,password):
    print(f"name: {name}")
    print(f"gmail: {gmail}")
    print(f"password: {password}")
display(name="Deepu",gmail="deepu@gmail.com",password="deepu@2215")
display(password="deepu@2215",name="Deepu",gmail="deepu@gmail.com")
display(gmail="deepu@gmail.com",password="deepu@2215",name="Deepu")

#Default arguments : these should be placed at the end of the function defination.
#we need to provide default values for the parameters in case the user does not provide any value for that parameter.
def display(name,gmail='deepu@gmail.com',password=''):
    print(f"name: {name}")
    print(f"gmail: {gmail}")
    print(f"password: {password}")
display("Deepu","deepu@gmail.com","deepu@2215")
display("Deepu","deepu@gmail.com")
display("Deepu","deepu@2215") 

#Variable aruguments : These are used when we do not know how many arguments will be passed to the function.
#we can use *args to pass a variable number of arguments to a function. The arguments are passed as a tuple.
def display(*names):
    print(names)
display('Deepu')
display('Deepu','Pallavi')
display('Deepu','Pallavi','naimisha')

# To print Keyword Variable Length Arguments (**kwargs).
#the arguments are passed as a dictionary.
#these are used when we do not know how many keyword arguments will be passed to the function.
def display(**products):
    print(products)
display(bag=5000)
display(bag=5000,book=30)
display(bag=5000,book=30,bottle=10)
'''
