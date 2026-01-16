from strands.tools import tool
from app.aws.adapters.knowledgebase_adapter import KnowledgeAdapter
knowledge_adapter = KnowledgeAdapter()


@tool(
    name="knowledge_base_query",
    description="Consulta a base de conhecimento para responder perguntas sobre o resort.",
)
def knowledge_base_query(question: str) -> str:
    return knowledge_adapter.query(question)