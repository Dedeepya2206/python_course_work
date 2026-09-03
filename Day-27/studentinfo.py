'''
import json
with open("data.json",'r') as file:
    data=json.load(file)
    print(data)
    print(data["username"])

#with open("data.json",'w') as  file:

import json
with open("data.json",'r') as file:
    data=json.load(file)
data["username"]="Dedeepya"
data["skills"].append("flask")
with open("data.json",'w') as file:
    json.dump(data,file,indent=4)
'''
import json
student={
    "name":"Dedeepya",
    "age":22,
    "Course":"Python"
}
json_data=json.dumps(student)
print(json_data)
student=json.loads(json_data)
print(student)
print(type(student))