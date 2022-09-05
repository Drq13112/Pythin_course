# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import requests

url="http://127.0.0.1:8000/items/"
r=requests.post(url)
d=r.json()
print(d)