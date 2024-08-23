from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):

    first_name:str = Field(...,)
    last_name:str = Field(...,)
    email:EmailStr = Field(...,)

class UserResponse(BaseModel):

    id:int
    first_name:str
    last_name:str
    email:str

class UserUpdate(BaseModel):

    first_name:str = Field(None)
    last_name:str = Field(None)
    email:EmailStr = Field(None)