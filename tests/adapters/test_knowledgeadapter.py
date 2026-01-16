from dotenv import load_dotenv
load_dotenv()
from app.aws.adapters.knowledgebase_adapter import KnowledgeAdapter

adapter = KnowledgeAdapter()

response = adapter.query("me fale sobre os tipos de quarto que o resort oferece")
print(response)