<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Authors: David Redondo Quintero & Mariano Álvarez

Practical use of a JSON script for web servicies
"""
#First of all, we import the json lib
import json


#A simple code of how json works
data='''{
    "name" : "David",
    "phone" : {
        "type" : "intl",
        "number" : "+34 666 66 66 66"
        },
        "email" : {
            "hide" : "No",
            "direction" : "davidjson@gmail.com"
        }
    }'''

# Converting the JSON file into a python dictionary
info= json.loads(data)
print("Example 1: ")
print('Name:', info["name"])

if "No"==(info["email"]["hide"]):
    print('Direction:',info["email"]["direction"])
else:
    print("Direction hiden")
print(" ")

#Let's code a little more complex example
#For this case, we will iterate a few times over the json data 
#Notice that we have changed the curly brackets to regular brackets,
#but only the brackets which capture the rest of the data.

data= '''[
        {
        "name" : "David",
        "phone" : {
            "type" : "intl",
            "number" : "+34 666 66 66 66"
            },
        "email" : {
            "hide" : "No",
            "direction" : "davidjson@gmail.com"
            }
        },
        {
        "name" : "Pedro",
        "phone" : {
            "type" : "intl",
            "number" : "+34 666 66 66 67"
            },
        "email" : {
            "hide" : "Yes",
            "direction" : "Pedrojson@gmail.com"
            }
        }
    ]'''
    
info= json.loads(data)
print("Example 2: ")
print('User count:', len(info))
for user in info :
    print("User:", user["name"])
    
    if "No"==(user["email"]["hide"]):
        print('Direction:',user["email"]["direction"])
    else:
        print("Direction hiden") 

# That was pretty useful, but in a real case we won't paste a JSON text inside
# of our script, so let's automate it. Be careful with the place where you save
# the file which you will read. It must be in the same directory as our script.
# Otherwise, we will have to specify the file path.

# We will use a method from the JSON library:
with open("myjsonfile.json") as file:
    # Notice that we have used "load" and not "loads". It's because they are little different
    # between them. The first one is used to read a JSON file and the second one to read a 
    # string
    
    data = json.load(file)

print('Orders number:', len(info))
i=0
for order in data["orders"] :
    i=i+1
    print("Client",i,"'s personal data:", order["client"])
    print("")
=======
# -*- coding: utf-8 -*-
"""
Authors: David Redondo Quintero & Mariano Álvarez

Practical use of a JSON script for web servicies
"""
#First of all, we import the json lib
import json


#A simple code of how json works
data='''{
    "name" : "David",
    "phone" : {
        "type" : "intl",
        "number" : "+34 666 66 66 66"
        },
        "email" : {
            "hide" : "No",
            "direction" : "davidjson@gmail.com"
        }
    }'''

# Converting the JSON file into a python dictionary
info= json.loads(data)
print("Example 1: ")
print('Name:', info["name"])

if "No"==(info["email"]["hide"]):
    print('Direction:',info["email"]["direction"])
else:
    print("Direction hiden")
print(" ")

#Let's code a little more complex example
#For this case, we will iterate a few times over the json data 
#Notice that we have changed the curly brackets to regular brackets,
#but only the brackets which capture the rest of the data.

data= '''[
        {
        "name" : "David",
        "phone" : {
            "type" : "intl",
            "number" : "+34 666 66 66 66"
            },
        "email" : {
            "hide" : "No",
            "direction" : "davidjson@gmail.com"
            }
        },
        {
        "name" : "Pedro",
        "phone" : {
            "type" : "intl",
            "number" : "+34 666 66 66 67"
            },
        "email" : {
            "hide" : "Yes",
            "direction" : "Pedrojson@gmail.com"
            }
        }
    ]'''
    
info= json.loads(data)
print("Example 2: ")
print('User count:', len(info))
for user in info :
    print("User:", user["name"])
    
    if "No"==(user["email"]["hide"]):
        print('Direction:',user["email"]["direction"])
    else:
        print("Direction hiden") 

# That was pretty useful, but in a real case we won't paste a JSON text inside
# of our script, so let's automate it. Be careful with the place where you save
# the file which you will read. It must be in the same directory as our script.
# Otherwise, we will have to specify the file path.

# We will use a method from the JSON library:
with open("myjsonfile.json") as file:
    # Notice that we have used "load" and not "loads". It's because they are little different
    # between them. The first one is used to read a JSON file and the second one to read a 
    # string
    
    data = json.load(file)

print('Orders number:', len(info))
i=0
for order in data["orders"] :
    i=i+1
    print("Client",i,"'s personal data:", order["client"])
    print("")
>>>>>>> 94cc937c85286f9ae8e1f0ecb5cd73312d4a6149
