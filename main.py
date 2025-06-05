# PACKAGE IMPORTS 
from typing import Union 
from fastapi import FastAPI
from typing import Annotated
from pydantic import EmailStr, StringConstraints
from passlib.context import CryptContext
from schema import userReg

# CREATE THE APP OBJECT
app = FastAPI()

# PASSWORD HASHING CONTEXT 	
pawPrint = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ROUTES
@app.get("/")
def root():
		return {"message": "Welcome to the Paba.io Brain. Purr-fect timing :)"}

# REGISTER ENDPOINT
@app.post("/register")
def userRegistration(user: userReg):
	# TRIM AND BASIC INPUT CHECK 	
	if not user.name.strip() or not user.password.strip():
		raise HTTPException(status_code=400, detail="Name and Password cannot be blank.")

	# HASH THE PASSWORD
	hash = pawPrint.hash(user.password)

	# TODO: SAVE USER TO DATABASE (not implemented in this example)
	print(f"Creating user: {user.name}, Email: {user.email}, Password Hash: {hash}")

	# RETURN SUCCESS MESSAGE
	return {"message": "User registered successfully", "name": user.name, "email": user.email}

