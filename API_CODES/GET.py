# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import requests

url = "http://127.0.0.1:8000/users/me"
r = requests.get(url)
d=r.json()
print(d)


user_id= 13112
r = requests.get(f'http://127.0.0.1:8000/users/{user_id}')
d=r.json()
print(d)
# Now let's use post method.
# We must define the body

data_form = {
    "name": "Hamburger",
    "description": "Sometimes a not really healthy food",
    "price": 7.99,
    "tax": 2
}

url="http://127.0.0.1:8000/items/"
res = requests.post('http://localhost:8000/items/',
    headers = {
        'Content-type': 'application/json'
    },json=data_form)


print(res.json())
