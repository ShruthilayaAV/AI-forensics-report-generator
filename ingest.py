import chromadb
import os

# 1. Setup the database
# This will create a folder named 'chroma_db' to store your knowledge
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="security_expert_kb")

# 2. Function to load your txt files
def ingest_data():
    kb_dir = "./knowledge_base"
    for i, filename in enumerate(os.listdir(kb_dir)):
        if filename.endswith(".txt"):
            with open(os.path.join(kb_dir, filename), "r") as f:
                content = f.read()
                # Store the text in the vector database
                collection.add(
                    documents=[content],
                    ids=[f"doc_{i}"]
                )
    print("✅ Knowledge base ingested into ChromaDB!")

if __name__ == "__main__":
    ingest_data()
