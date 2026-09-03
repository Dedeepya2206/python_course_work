import re
'''
#To validate a full name
fullname=input("Enter your full name:")
pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res=re.fullmatch(pattern,fullname)
print("Valid Fullname" if res else "Invalid fullname")

#To validate an email address
email=input("Enter your email address:")
pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
res=re.fullmatch(pattern,email)
print("Valid Email" if res else "Invalid Email")

#To validate a phone number
phone_number = input("enter your phone number: ")
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
res = re.fullmatch(pattern, phone_number)
print("Valid phone_number" if res else "Invalid phone_number")

#To validate a password
password = input("Enter your password:")
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
res = re.fullmatch(pattern, password)
print("Valid password" if res else "Invalid password")

#To validate a instagram username
username = input("Enter your Instagram username: ")
pattern = r'^[a-zA-Z0-9._]{2,15}$'
res = re.fullmatch(pattern, username)
print("Valid Instagram Username" if res else "Invalid Instagram username")


#To validate a adharcard number
aadharcard_number = input("Enter your Aadhar card number:")
pattern = r'^\d{4}\s\d{4}\s\d{4}$'
res = re.fullmatch(pattern, aadharcard_number)
print("Valid Aadhar card number" if res else "Invalid Aadhar card number")
'''
#To validate a PAN card number
pancard_number = input("Enter your PAN card number:")
pattern = r'^[A-Z]{5}\d{4}[A-Z]{1}$'
res = re.fullmatch(pattern, pancard_number)
print("Valid PAN card number" if res else "Invalid PAN card number")

