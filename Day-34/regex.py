import re
'''
pattern = r'code'
text = 'Codegnan'

res = re.match(pattern,text)
print(res.group() if res else "Pattern not found")

pattern = r'[0-9]'
text = 'Codegnan'

res = re.match(pattern,text)
print(res.group() if res else "Pattern not found")

pattern = r'[a-zA-z]'
text = 'Codegnan'

res = re.match(pattern,text)
print(res.group() if res else "Pattern not found")


pattern = r'C'
text = 'Codegnan'

res = re.match(pattern,text)
print(res.group() if res else "Pattern not found")

#search
pattern = r'[0-9]'
text = 'Codegnan2026'

res = re.search(pattern,text)
print(res.group() if res else "Pattern not found")

pattern = r'[0-9]'
text = 'Codegnan2026'

#findall
res = re.findall(pattern,text)
print(res)

pattern = r'[a-zA-Z]'
text = 'Codegnan 2026'

res = re.findall(pattern,text)
print(res)

pattern = r'[0-9A-za-z]'
text = 'Codegnan 2026'

res = re.findall(pattern,text)
print(res)

#finditer
pattern = r'[a-zA-Z0-9]'
text = 'Codegnan 2026 Python version 3.14'

res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())

#fullmatch is a for validation

pattern = r'[0-9] {10}'
text = '9876543210'

res = re.fullmatch(pattern,text)
print(res.group() if res else "Pattern not found")

#split()
pattern = r'[,#(]'
text = 'java,python(html#css'

res = re.split(pattern,text)
print(res)

#sub
pattern = r'[a-z]'
text = 'python version 3.14, batch-63'

res = re.sub(pattern,'*',text)
print(res)


#metacharacters
#. 
pattern = r'e.t'
text = 'e@t eaat eat eet ect egfhjet hgjeokj'

res = re.findall(pattern,text)
print(res)

#^ start with
pattern = r'^[0-9]'
text = '0987654321'

res = re.findall(pattern,text)
print(res)

pattern = r'^(91)'
text = '9187654321'

res = re.findall(pattern,text)
print(res)

#endswith $
pattern = r'9$'
text = '0876543219'

res = re.findall(pattern,text)
print(res)

pattern = r'81$'
text = '8765432191'

res = re.findall(pattern,text)
print(res)

# *:zero or more occurance
pattern = r'to*'
text = 'to t too toooo tooooooo tgoogh toogh'

res = re.findall(pattern,text)
print(res)

# +:one or more occurance
pattern = r'to+'
text = 'to t too toooo tooooooo tgoogh toogh'

res = re.findall(pattern,text)
print(res)

pattern = r'ab*'
text = 'ab abbb a abbbb abbbbba'

res = re.findall(pattern,text)
print(res)

pattern = r'ab+'
text = 'ab abbb a abbbb abbbbba'

res = re.findall(pattern,text)
print(res)
#?
pattern = r'colo?rs'
text = 'colours'

res = re.findall(pattern,text)
print(res)

#or
pattern = r'91|0'
text = '91'

res = re.findall(pattern,text)
print(res)

pattern = r'91|0'
text = '0'

res = re.findall(pattern,text)
print(res)

pattern = r'91|0'
text = '879'

res = re.findall(pattern,text)
print(res)
'''
# Character Classes
import re
pattern = r'[aeiou]'    # Zero or one occurrence
text = 'codegnan programming' 
res = re.findall(pattern,text)            
print(res)