from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
from fastapi import FastAPI
from fastapi import Response
from app.agent.orchestrator_agent import route


app = FastAPI(title="Hotel AI Agent")
class MessageRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(message: MessageRequest):
    response = await route(message.message)
    return Response(content=response, media_type="text/plain; charset=utf-8")
    #return {"response": await route(message.message)}