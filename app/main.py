from typing import Union

from fastapi import FastAPI

import datetime
import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/mock/mulesoft/queue/{q_name}")
def read_queue(q_name: str):
# go find some values
# result payload should look like this
#
# {
#        "destination": "Queue1",
#        "messages": 7,
#        "inflightMessages": 0
#    }

    now = datetime.datetime.now()

    if "_hr" in q_name:
        messages = now.minute + int(now.second/15)
        inflightMessages = random.randint(0,int(now.second/15))

    elif "_15" in q_name:
        messages = now.minute%15
        inflightMessages = random.randint(0,messages%4)

    else:
        messages = now.hour * 60 + now.minute
        inflightMessages = random.randint(0,20)

    return {"destination": q_name, "messages": messages, "inflightmessages": inflightMessages}

