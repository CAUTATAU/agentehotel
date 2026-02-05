from strands.models.bedrock import BedrockModel
from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import AgentCoreMemorySessionManager


bedrockModel = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    guardrail_id="arn:aws:bedrock:us-east-1:699475929122:guardrail/9bxf9dspgs52",
    guardrail_version="2",
    guardrail_trace="enabled"
)