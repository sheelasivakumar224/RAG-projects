from app.database import get_collection

def add_sample_documents():
    collection = get_collection()
    collection.upsert(
        documents=[
            "Photosynthesis is the process used by plants to convert light energy into chemical energy.",
            "Chlorophyll is the green pigment found in plants that absorbs sunlight during photosynthesis.",
            "The financial market experienced a significant downturn due to unexpected inflation rates.",
            "Cellular respiration is how cells derive energy from organic molecules."
        ],
        ids=["doc1", "doc2", "doc3", "doc4"]
    )

def search_documents(query_text: str, n_results: int = 2):
    collection = get_collection()
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    return results