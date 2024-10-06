
'''

[ FAISS 유사도 검색 수행 코드 ]

'''

import torch
from transformers import BertTokenizer, BertModel
import faiss

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

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(query_embedding, k)
        return distances, indices

with open("dataset_source_text_all.txt", "r", encoding="utf-8") as f:
    texts = [line.strip() for line in f.readlines()]

searcher = TextSearch()

embeddings = searcher.encode(texts)
searcher.create_faiss_index(embeddings)

with open("dataset_for_faiss_search.txt", "r", encoding="utf-8") as question_file:
    for question in question_file:
        question = question.strip()  
        question_embedding = searcher.encode([question])  

        k = 7
        distances, indices = searcher.search(question_embedding, k=k)  

        # 결과를 한 줄로 저장 (유사한 순서대로 "1. 문장, 2. 문장, ..." 형태)
        with open("faiss_embedding.txt", "a", encoding="utf-8") as result_file:
            formatted_texts = [f"{rank}. {texts[idx]}" for rank, idx in enumerate(indices[0], start=1)]
            result_file.write(', '.join(formatted_texts) + "\n")

print("----<유사한 문장 추출 완료>----")
