from strands import Agent
from app.mcp.tools.knowledge_tool import knowledge_base_query
from app.agent.util.invoke_model import bedrockModel

conversational_agent = Agent(
    name="Conversational Agent",
    model=bedrockModel,
    tools=[knowledge_base_query],
    system_prompt="Você é um assistente virtual especializado em fornecer informações sobre o resort com base na base de conhecimento disponível."
)