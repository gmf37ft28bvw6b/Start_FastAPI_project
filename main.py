from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

from user.router_user import router_user
from message.router_message import router_message
from chat.router_chat import router_chat
app = FastAPI()

@app.get("/docs")
def swagger():
    print("svfss")
    return get_swagger_ui_html(openapi_url="/openapi.json",title="messanger_api")



app.include_router(router_user)
app.include_router(router_message)
app.include_router(router_chat)











