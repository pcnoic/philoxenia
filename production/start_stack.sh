#!/usr/bin/env bash

API_LOCATION="/api"
CLIENT_LOCATION="/client"


cd ${API_LOCATION}
gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --workers 1 --threads 8 --timeout 0 api:app &

