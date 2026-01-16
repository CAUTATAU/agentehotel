from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
from fastapi import FastAPI
from app.agent.orchestrator_agent import route


app = FastAPI(title="Hotel AI Agent")
class MessageRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(message: MessageRequest):
    return {"response": await route(message.message)}