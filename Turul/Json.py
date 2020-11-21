# -*- coding: utf-8 -*-

import json

# data = '{"Firstname":"Atakan","Lastname":"Özen","Age":"24","FavSinger":"Feyruz","AssStatus":"Fat"}'
# jsondata = json.loads(data)
# print(type(jsondata))

with open("users.json") as users:
    data = json.load(users)
    for i in range(2):
        print(data[i]["username"])
        print(data[i]["address"]["street"])
        
     
    