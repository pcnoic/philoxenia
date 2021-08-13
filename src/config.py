"""
    config.py
    Configuration values for Philoxenia
    
    GNU GENERAL PUBLIC LICENSE
"""


# TODO: make this read params from environment variables
class ConfigParams:
    MONGODB_HOST = "mongodb://localhost:27017" # protect with basic auth
    MONGODB_NAME = "philoxenia_store"
    DEV_URL = "http://localhost:8000"
