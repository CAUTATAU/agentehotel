from strands import Agent
from app.agent.conversational_agent import conversational_agent
from app.agent.booking_agent import booking_agent

router = Agent(
    model="anthropic.claude-3-5-sonnet-20240620-v1:0",
    system_prompt="""
Classifique a intenção:
KNOWLEDGE ou BOOKING.
Responda apenas uma palavra.
"""
)

async def route(message: str) -> str:
    response =  await router.invoke_async(message)
    intent = response.message['content'][0]['text']
    if intent == "KNOWLEDGE":
        result =  await conversational_agent.invoke_async(message)
        return result.message["content"][0]['text']
    if intent == "BOOKING":
        result =  await booking_agent.invoke_async(message)
        return result.message["content"][0]['text']

    return "Não consegui entender sua solicitação."
