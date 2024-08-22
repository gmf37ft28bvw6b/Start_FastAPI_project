from pydantic import BaseModel



class CreateUserDto(BaseModel):
    name: str
    surname: str
    email: str
    phone: str
    password_hash: str


