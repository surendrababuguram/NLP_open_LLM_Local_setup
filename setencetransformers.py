from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

Sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
Sentence_model.save_pretrained("/opt/all-MiniLM-L6-v2")
