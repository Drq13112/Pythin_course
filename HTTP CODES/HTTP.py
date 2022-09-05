
"""
@authors: David Redondo and Mariano Álvarez
Introducing to request lib and how HTTP works
"""

import time
import requests

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

search_term = "python"
r = requests.get(f'https://en.wikipedia.org/wiki/{search_term}')
r.raise_for_status()
with open('Python.html', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=50000):
        fd.write(chunk)

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

url = 'https://docs.google.com/forms/d/e/1FAIpQLSeSE57fVkrI63HdPthXXk-d-a6Nh60NhMxbGYF2dODrusu1Iw/formResponse'
form_data = {"entry.1756925075":"David","fvv":1,"draftResponse":'[]',"pageHistory":0,"fbzx":5401894740644093047}
r=requests.post(url, data=form_data)  

print(r) # response [200]

"""
Send the POST request to the https://httpbin.org website using 
the post() method and print the response.
"""

res = requests.post('https://httpbin.org/post',
                    data={'My name': 'Mariano Alvarez'})
print(res.content)

# Now we are gonna do a request "post" to send data. It's pretty similar than
# the previous method. Esta parte del codigo es una ejemplo del libro WEB Scraping


import requests
# We create a dictionary where we will save our data
params = {'firstname': 'David', 'lastname': 'Redondo'}

# Notice there is a optional field where we can upload the dictionary created

response = requests.post(
    'http://pythonscraping.com/pages/processing.php')

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
