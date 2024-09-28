import os

folder_path = './original_dataset'

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        try:
            # 기본적으로 utf-8로 시도
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
        except UnicodeDecodeError:
            # utf-8 실패 시 cp949로 다시 시도
            with open(file_path, 'r', encoding='cp949') as file:
                content = file.read()

        new_content = '\n'.join([line for line in content.splitlines() if line.strip() != ''])

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

print("모든 txt 파일의 중복된 줄바꿈을 처리하였습니다.")
