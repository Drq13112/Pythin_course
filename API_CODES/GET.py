# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import requests

url="http://127.0.0.1:8000/users/13112"
r=requests.get(url)
d=r.json()
print(d)