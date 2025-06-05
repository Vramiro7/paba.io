# Pydanctic schema for Paba.io
from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated

# Create a Pydantic model for user registration
class userReg(BaseModel):
    name: str
    email: EmailStr
    password: Annotated[
    	str,
    	StringConstraints(min_length=8)
		]
