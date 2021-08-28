#!/usr/bin/env bash

API_LOCATION="/api"

cd ${API_LOCATION}
gunicorn -k uvicorn.workers.UvicornWorker -b unix:/tmp/gunicorn.sock -w 1 --threads=8 --timeout=0 api:app &
echo "Philoxenia API has been started."

nginx -g "daemon off;"