'''
openai embedding을 써야함.
그냥 무료 gemini embedding써볼까
'''
import os

os.environ["OPENAI_API_KEY"] = "sk-"
os.environ["NEO4J_URI"] = "neo4j+s://demo.neo4jlabs.com"
os.environ["NEO4J_USERNAME"] = "companies"
os.environ["NEO4J_PASSWORD"] = "companies"
os.environ["NEO4J_DATABASE"] = "companies"

embeddings = OpenAIEmbeddings()
graph = Neo4jGraph()
vector_index = Neo4jVector.from_existing_index(
    embeddings, 
    index_name="news"
)