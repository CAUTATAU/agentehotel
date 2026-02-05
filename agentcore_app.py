from bedrock_agentcore.runtime import BedrockAgentCoreApp
from app.agent.orchestrator_agent import route

app = BedrockAgentCoreApp()
@app.entrypoint
async def agent_invocation(payload, context):
    """
    AgentCore Runtime entrypoint.
    Recebe: {"prompt": "..."} via POST /invocations
    Retorna: {"result": "...", "format": "markdown", "data": {...}}

    """
    user_message = payload.get("prompt", "")
    if not user_message:
        return {"error": "No prompt found in input. Send JSON with key 'prompt'."}
    # Strands pode retornar string, objeto com .message, ou lista [{text:...}]
    result = await route(user_message)
    print("context:\n-------\n", context)
    print("result:\n*******\n", result)
    return {
        "format": "markdown",
        "result": result,
    }
app.run()