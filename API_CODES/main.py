#Concatenate the following strings
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

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


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


    