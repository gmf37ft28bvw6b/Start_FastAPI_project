from random import randint
from fastapi import APIRouter

from dto.CreateUserDto import CreateUserDto

router_user = APIRouter()

users_list_array = [
{"id": 1, "name": "Dan","surname": "Dan","email": "Dan","phone": "+7","password_hash":"sjv"},
{"id": 2, "name": "Dan","surname": "Dan","email": "Dan","phone": "+7","password_hash":"sjv"},
{"id": 3, "name": "Dan","surname": "Dan","email": "Dan","phone": "+7","password_hash":"sjv"},
{"id": 4, "name": "Dan","surname": "Dan","email": "Dan","phone": "+7","password_hash":"sjv"},
{"id": 5, "name": "Dan","surname": "Dan","email": "Dan","phone": "+7","password_hash":"sjv"}
]




@router_user.get("/user")
async def get_user_list ():
    return users_list_array



@router_user.get("/user/{id}")
async def get_user(id):
    user = list(filter(lambda user: (user["id"] == int(id)), users_list_array))[0]
    return user









@router_user.post("/user")
async def create_user(new_user:CreateUserDto):
    new_user_id = randint(1,200)
    users_list_array.append(
        {"id": new_user_id, "name": new_user.name, "surname": new_user.surname, "email": new_user.email, "phone": new_user.phone, "password_hash": new_user.password_hash}
    )
    return new_user_id



@router_user.delete("/user")
async def delete_user(id):
    return id



@router_user.put("/user")
async def update_user():
    return {}



