
"""

[ 원문 데이터를 slidingwindow 데이터로 분할하는 코드 ]

"""

import os

def extract_sentences(input_file, output_file):

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    result = []
    
    start_index = 0
    end_index = 14
    while start_index < len(lines):

        # result.append(input_subject + '\n')  # 원하는 문장 추가
        chunk = lines[start_index:end_index]
        result.extend(chunk)
        result.append('\n')  
        
        start_index += 7
        end_index += 7
        
        if end_index > len(lines):

            # result.append('\n' + input_subject + '\n')
            result.extend(lines[-7:])  
            result.append('\n')
            break

    with open(output_file, 'a', encoding='utf-8') as file:
        file.writelines(result)

# extract_sentences(input_file_path, output_file_path, input_subject)

input_folder_path = './original_dataset'
output_folder_path = './sliding_window'

for filename in os.listdir(input_folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder_path, filename)
    
    input_file_path = file_path
    output_file_path = output_folder_path + "/" + os.path.splitext(filename)[0] + "_sw.txt"
    extract_sentences(input_file_path, output_file_path)