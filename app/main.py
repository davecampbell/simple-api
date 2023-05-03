from typing import Union

from fastapi import FastAPI

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

    messages = 7
    inflightMessages = 0

    return {"destination": q_name, "messages": messages, "inflightmessages": inflightMessages}


