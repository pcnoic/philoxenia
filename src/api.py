"""
Philoxenia - P2P Space Exchange
MIT LICENSE
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

from models.space import *
from xenia.db import DBSpaces



# Application Controllers
app = FastAPI()

# Configure CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logic Controllers
dbspaces = DBSpaces()

# Endpoints
@app.get("/api/v1/up")
def up():
    response = json.dumps({"status": "alive"})
    return response

@app.post("/api/v1/space/add")
def add_space(space_offer: SpaceOffer):
    result = dbspaces.write(space_offer.dict())
    if result == 0:
        response = json.dumps({"status": "success"})
    else:
        response = json.dumps({"status": "fail"})
    
    return response

@app.post("/api/v1/space/request")
def request_space(space_request: SpaceRequest):
    result = dbspaces.find(space_request.dict())
    if len(result) is not 0:
        response = result
    else:
        response = json.dumps({"status": "no_results"})
    
    return response

@app.get("/api/v1/space/latest")
def get_latest_spaces():
    result = dbspaces.latest()
    if result is not None:
        response = result
    else:
        response = json.dumps({"status":"no_results"})
    
    return response
