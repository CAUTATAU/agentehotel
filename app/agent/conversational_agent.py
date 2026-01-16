from strands import Agent
from app.mcp.tools.knowledge_tool import knowledge_base_query

conversational_agent = Agent(
    name="Conversational Agent",
    model="anthropic.claude-3-5-sonnet-20240620-v1:0",
    tools=[knowledge_base_query],
    system_prompt="Você é um assistente virtual especializado em fornecer informações sobre o resort com base na base de conhecimento disponível."
)