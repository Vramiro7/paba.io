# PACKAGE IMPORTS 

from typing import Union 
from fastapi import FastAPI


# CREATE THE APP OBJECT

app = FastAPI()

@app.get("/")

def root():
	return {"message" : "Welcome to the Paba.io Brain. Purr-fect timing :)"}

