"""
    config.py
    Configuration values for Philoxenia
    
    GNU GENERAL PUBLIC LICENSE
"""
import os

class ConfigParams:
    MONGODB_HOST = os.environ["MONGODB_HOST"]
    MONGODB_NAME = os.environ["MONGODB_NAME"]
    DEV_URL = "http://localhost:8000"
