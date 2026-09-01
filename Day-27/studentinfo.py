'''
import json
with open("data.json",'r') as file:
    data=json.load(file)
    print(data)
    print(data["username"])

#with open("data.json",'w') as  file:
'''
import json
with open("data.json",'r') as file:
    data=json.load(file)
data["username"]="Dedeepya"
data["skills"].append("flask")
with open("data.json",'w') as file:
    json.dump(data,file,indent=4)