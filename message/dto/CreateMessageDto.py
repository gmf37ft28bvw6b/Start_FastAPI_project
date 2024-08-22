from pydantic import BaseModel



class CreateMessageDto(BaseModel):
    text_content: str
    time_created: str
    owner_id: str
    chat_id: str














