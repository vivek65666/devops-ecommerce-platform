import os, time
from typing import Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
SERVICE_NAME=os.getenv("SERVICE_NAME","user-service")
app=FastAPI(title=f"{SERVICE_NAME} API",version="1.0.0")
Instrumentator().instrument(app).expose(app)
START=time.time(); ITEMS=[]
class Item(BaseModel):
    name:str
    value:str|None=None
@app.get("/health")
def health(): return {"status":"ok","service":SERVICE_NAME,"uptime_seconds":round(time.time()-START,2)}
@app.get("/ready")
def ready(): return {"ready":True,"service":SERVICE_NAME}
@app.get("/api/v1/users")
def list_items(): return {"service":SERVICE_NAME,"items":ITEMS}
@app.post("/api/v1/users",status_code=201)
def create_item(item:Item):
    record={"id":len(ITEMS)+1,**item.model_dump()}; ITEMS.append(record); return record
@app.get("/api/v1/users/{item_id}")
def get_item(item_id:int):
    for item in ITEMS:
        if item["id"]==item_id:return item
    raise HTTPException(404,"Item not found")
