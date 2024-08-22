from random import randint
from fastapi import APIRouter

from message.dto.CreateMessageDto import CreateMessageDto

router_message = APIRouter()


message_list_array = [
{"id": 1, "text_content": "test message","time_created": "Dan","owner_id": "34","chat_id": "88",},
{"id": 2, "text_content": "test message","time_created": "Dan","owner_id": "34","chat_id": "88",},
{"id": 3, "text_content": "test message","time_created": "Dan","owner_id": "34","chat_id": "88",},
{"id": 4, "text_content": "test message","time_created": "Dan","owner_id": "34","chat_id": "88",},
{"id": 5, "text_content": "test message","time_created": "Dan","owner_id": "34","chat_id": "88",},
]




@router_message.get("/message")
async def get_message_list ():
    return message_list_array



@router_message.get("/message/{id}")
async def get_message(id):
    # 1)   проверить, что id - число (проверка на тип, число больше 0). 2) если сообщение не найдено, возврат сообщения метку
    message = list(filter(lambda message: (message["id"] == int(id)), message_list_array))[0]

    return message



@router_message.post("/message")
async def create_message(new_message: CreateMessageDto):
    new_message_id = randint(1, 200)
    message_list_array.append(
        {"id": new_message_id, "text_content": new_message.text_content,"time_created": new_message.time_created,"owner_id": new_message.owner_id,"chat_id": new_message.chat_id}
    )
    return new_message_id




@router_message.delete("/message/{id}")
async def delete_message(id):

    # как удалить элемент массива по id (GPT),
    # message_list_array = list(filter(lambda message: (message["id"] != int(id)), message_list_array))[0]
    return id



@router_message.put("/message")
async def update_message():
    # заменить элемент массива
    return {}














