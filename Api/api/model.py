from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
model.save("local_models/paraphrase-MiniLM-L6-v2")
