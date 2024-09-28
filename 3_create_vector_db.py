import os
import torch
from transformers import BertTokenizer, BertModel
import faiss
from slugify import slugify  # slugify 라이브러리 사용

class TextSearch:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name).eval()

    def encode(self, texts):
        with torch.no_grad():
            inputs = self.tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=128)
            outputs = self.model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1)
        return embeddings.numpy()

    def create_faiss_index(self, embeddings):
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

    def save_faiss_index(self, index_path):
        faiss.write_index(self.index, index_path)

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(query_embedding, k)
        return distances, indices


input_folder_path = './original_dataset'
output_folder_path = './vector_db'

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

for filename in os.listdir(input_folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            texts = [line.strip() for line in f.readlines()]

        searcher = TextSearch()

        embeddings = searcher.encode(texts)
        searcher.create_faiss_index(embeddings)

        # 파일 이름을 ASCII로 변환하여 안전한 저장 이름으로 변경
        index_filename = slugify(os.path.splitext(filename)[0]) + ".index"
        index_file_path = os.path.join(output_folder_path, index_filename)

        searcher.save_faiss_index(index_file_path)

        print(f"FAISS 인덱스 파일 저장 완료: {index_file_path}")
