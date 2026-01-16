from app.aws.bedrock_client import get_bedrock_client
from app.config.config import KNOWLEDGE_BASE_ID

class KnowledgeAdapter:
    def __init__(self):
        self.client = get_bedrock_client()

    def query(self, question: str) -> str:
        response = self.client.retrieve(
            knowledgeBaseId=KNOWLEDGE_BASE_ID,
            retrievalQuery={
                "text": question
            }
        )

        contents = [r["content"]["text"] for r in response.get("retrievalResults", [])]
        return "\n\n\n".join(contents)
