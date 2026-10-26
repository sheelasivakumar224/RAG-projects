import chromadb

def get_chroma_client():
    return chromadb.PersistentClient(path="./chroma_db")

def get_collection():
    client = get_chroma_client()
    return client.get_or_create_collection(name="semantic_search_collection")