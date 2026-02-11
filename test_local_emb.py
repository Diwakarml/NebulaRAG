try:
    from sentence_transformers import SentenceTransformer
    print("Import successful. Loading model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    print("Model loaded.")
    emb = model.encode("test")
    print(f"Embedding successful. Dim: {len(emb)}")
except Exception as e:
    print(f"Error: {e}")
