import os
import google.generativeai as genai

genai.configure(api_key='AIzaSyA_MP43Ck_-iKJkwlw6rIi0OGRMAxBBQFg')

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

input_folder_path = "./QA_dataset"
output_file_path = "./metadata/"

# 질문 리스트를 저장할 리스트

result = ""
for filename in os.listdir(input_folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder_path, filename)
    
    questions = []
    # 텍스트 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("Question:"):
                questions.append(line)
    
    responses = []
    for q in questions:    
        prompt = q + "Give me topic about this question."
        response = chat_session.send_message(prompt)

        responses.append(response.text)
        print(response.text)

    result = "\n".join(responses)
    with open(output_file_path+filename[:-4], 'w', encoding='utf-8') as file:
      file.write(result)