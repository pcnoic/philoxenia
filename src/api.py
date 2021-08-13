"""
Philoxenia - P2P Space Exchange
MIT LICENSE
"""

from fastapi import FastAPI
import json

from models.space import *
from xenia.db import DBSpaces



# Application Controllers
app = FastAPI()

# Logic Controllers
dbspaces = DBSpaces()

# Endpoints 
@app.post("/api/v1/space/add")
def add_space(space_offer: SpaceOffer):
    result = dbspaces.write(space_offer)
    if result == 0:
        response = json.dumps({"status": "success"})
    else:
        response = json.dumps({"status": "fail"})
    
    return response

@app.post("/api/v1/space/request")
def request_space(space_request: SpaceRequest):
    result = dbspaces.find(space_request)
    if result is not None:
        response = json.dumps(result)
    else:
        response = json.dumps({"status": "no_results"})
    
    return response

@app.get("/api/v1/space/latest")
def get_latest_spaces():
    result = dbspaces.latest()
    if result is not None:
        response = json.dumps(result)
    else:
        response = json.dumps({})
    
    return response
