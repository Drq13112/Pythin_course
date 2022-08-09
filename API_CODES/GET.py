# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import requests

url="http://127.0.0.1:8000/items/{TU}"
r=requests.get(url)
d=r.json()