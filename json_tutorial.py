'''
///python json translation of types///

Python          Json
dict            object
list, tuple     arrey
str             string
int,float,long  number
True            true
False           false
None            null

'''

import json

#converting python dict to json object

person = {"name": "jhon", "age": 30, "city": "NewYork", "hasChildern": False, "titles": ["engineer", "programmer"]}

#indent will keep the object nice to read and recomended is 4 and default is 1, sort_keys will sort the keys in object
person_JSON = json.dumps(person, indent=4, sort_keys= True)
print(person_JSON)

#dumping the data to file
#dumps = dump as a string
#dump = dump to file or variable

with open("person.json", "w") as file:
    json.dump(person, file, indent= 4)


#converting json to python
#loads = load from a string
#load = load ffrom file or variable
person = json.loads(person_JSON)
print("Python_Dict: ",person)

#get from a file

with open("example.json", "r") as file:
   person = json.load(file)

print("Python_Dict: ",person)
