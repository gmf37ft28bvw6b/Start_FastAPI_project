from random import randint
from fastapi import APIRouter

from dto.CreateChatDto import CreateChatDto

router_chat = APIRouter()


chat_list_array = [
{"id": 1, "name": "Dan","owner_id": "23"},
{"id": 2, "name": "Dan","owner_id": "2"},
{"id": 3, "name": "Dan","owner_id": "223"},
{"id": 4, "name": "Dan","owner_id": "233"},
{"id": 5, "name": "Dan","owner_id": "234"},
]


@router_chat.get("/chat")
async def get_chat_list ():
    return {}



@router_chat.get("/chat/{id}")
async def get_chat():
    return {}


@router_chat.post("/chat")
async def create_chat(new_chat:CreateChatDto):
    new_chat_id = randint(1, 200)
    chat_list_array.append(
        {"id": new_chat_id, "name": new_chat.name, "owner_id": new_chat.owner_id}
    )
    return new_chat_id



@router_chat.delete("/chat")
async def delete_chat(id):
    return id



@router_chat.put("/chat")
async def update_chat():
    return {}






