#Concatenate the following strings
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
"""
A web API is a part of a website designed to interact with programs that
use very specific URLs to request certain information. This kind of request

is called an API call. The requested data will be returned in an easily pro-
cessed format, such as JSON or CSV. Most apps that rely on external data

sources, such as apps that integrate with social media sites, rely on API calls.
"""
"""
When you need to send data from a client (let's say, a browser) to your API, 
you send it as a request body.

A request body is data sent by the client to the API. 
A response body is the data that the API sends to the client.

Our API almost always has to send a response body. 
But clients don't necessarily need to send request bodies all the time.

To declare a request body, 
we use Pydantic models with all their power and benefits.
"""

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    
app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


    
