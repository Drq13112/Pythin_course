<<<<<<< HEAD
"""
@authors: David Redondo and Mariano Álvarez
Introducing to request lib and how HTTP works
"""

import time
import requests
from flask import *

# Remember to install requests lib before starting


##########################################################
#                         GET                            #
##########################################################

   
r = requests.get('http://api.open-notify.org/astros.json')
print(r.json())

r = requests.get('http://github.com/Drq13112/Python_course')
# print(r.text)

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
data = r.json()

print("Abilities:")
for ability in data["abilities"]:
    print("-", ability["ability"]["name"])

print("name:", data['name'])

# More uses that we can give to this lib.
# Imagine that you want to create a app which need to check
# the ETH price periodly.
# In this case we can request it to a free trade API.
#
# This API only let us to access to the price each second,
# so becareful with the times you execute the code.

API_KEY = "c7efefa37c8e9416691d981b4d8e8cac1288bad1"

url = "https://api.nomics.com/v1/currencies/ticker?key=c7efefa37c8e9416691d981b4d8e8cac1288bad1&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&platform-currency=ETH&per-page=100&page=1"
r = requests.get(url)
data = r.json()
print("Name:", data[0]['name'])
print("Price at", time.ctime(), ":", data[0]['price'], "€")


##########################################################
#                         POST                           #
##########################################################

r = requests.post('https://en.wikipedia.org/w/index.php',
                    data={'search': 'Nanotechnology'})
r.raise_for_status()
with open('Nanotechnology.html', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=50000):
        fd.write(chunk)
# print(req.content)

"""
Send the POST request to the https://httpbin.org website using 
the post() method and print the response.
"""

res = requests.post('https://httpbin.org/post',
                    data={'My name': 'Mariano Alvarez'})

# Now we are gonna do a request "post" to send data. It's pretty similar than
# the previous method. Esta parte del codigo es una ejemplo del libro WEB Scraping


# We create a dictionary where we will save our data
params = {'firstname': 'David', 'lastname': 'Redondo'}

# Notice there is a optional field where we can upload the dictionary created

response = requests.post(
    'http://pythonscraping.com/pages/processing.php', data=params)
print(response.text)
print("")

"""
The HTML code of the form to fill out:
    
<form method="post" action="processing.php">

First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname"><br>

<input type="submit" value="Submit">

</form>
"""

# We can define a timeout to wait for the response:
response = requests.post(
    'http://pythonscraping.com/pages/processing.php', data=params, timeout=10)

# If the server doesn't sent a response before the time was gone, the system will
# send an exception. IN case we hadn't define a timeout, the system will be waiting until
# it gets the response.


# Now we are going to create our own server to who send requests:

=======
"""
@authors: David Redondo and Mariano Álvarez
Introducing to request lib and how HTTP works
"""

import time
import requests
from flask import *

# Remember to install requests lib before starting


##########################################################
#                         GET                            #
##########################################################

   
r = requests.get('http://api.open-notify.org/astros.json')
print(r.json())

r = requests.get('http://github.com/Drq13112/Python_course')
# print(r.text)

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
data = r.json()

print("Abilities:")
for ability in data["abilities"]:
    print("-", ability["ability"]["name"])

print("name:", data['name'])

# More uses that we can give to this lib.
# Imagine that you want to create a app which need to check
# the ETH price periodly.
# In this case we can request it to a free trade API.
#
# This API only let us to access to the price each second,
# so becareful with the times you execute the code.

API_KEY = "c7efefa37c8e9416691d981b4d8e8cac1288bad1"

url = "https://api.nomics.com/v1/currencies/ticker?key=c7efefa37c8e9416691d981b4d8e8cac1288bad1&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&platform-currency=ETH&per-page=100&page=1"
r = requests.get(url)
data = r.json()
print("Name:", data[0]['name'])
print("Price at", time.ctime(), ":", data[0]['price'], "€")


##########################################################
#                         POST                           #
##########################################################

r = requests.post('https://en.wikipedia.org/w/index.php',
                    data={'search': 'Nanotechnology'})
r.raise_for_status()
with open('Nanotechnology.html', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=50000):
        fd.write(chunk)
# print(req.content)

"""
Send the POST request to the https://httpbin.org website using 
the post() method and print the response.
"""

res = requests.post('https://httpbin.org/post',
                    data={'My name': 'Mariano Alvarez'})

# Now we are gonna do a request "post" to send data. It's pretty similar than
# the previous method. Esta parte del codigo es una ejemplo del libro WEB Scraping


# We create a dictionary where we will save our data
params = {'firstname': 'David', 'lastname': 'Redondo'}

# Notice there is a optional field where we can upload the dictionary created

response = requests.post(
    'http://pythonscraping.com/pages/processing.php', data=params)
print(response.text)
print("")

"""
The HTML code of the form to fill out:
    
<form method="post" action="processing.php">

First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname"><br>

<input type="submit" value="Submit">

</form>
"""

# We can define a timeout to wait for the response:
response = requests.post(
    'http://pythonscraping.com/pages/processing.php', data=params, timeout=10)

# If the server doesn't sent a response before the time was gone, the system will
# send an exception. IN case we hadn't define a timeout, the system will be waiting until
# it gets the response.


# Now we are going to create our own server to who send requests:

>>>>>>> 94cc937c85286f9ae8e1f0ecb5cd73312d4a6149
