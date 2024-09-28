
"""

[ 원문 데이터를 slidingwindow 데이터로 분할하는 코드 ]

"""

# source_text: 
input_file_path = "./ip15pro_en.txt"

# input_subject = "The following article is about the BMW XM."
output_file_path = "./ip15pro_slidingw_line6_test.txt"

def extract_sentences(input_file, output_file):

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    result = []
    
    start_index = 0
    end_index = 6
    while start_index < len(lines):

        # result.append(input_subject + '\n')  # 원하는 문장 추가
        chunk = lines[start_index:end_index]
        result.extend(chunk)
        result.append('\n')  
        
        start_index += 3
        end_index += 3
        
        if end_index > len(lines):

            # result.append('\n' + input_subject + '\n')
            result.extend(lines[-6:])  
            result.append('\n')
            break

    with open(output_file, 'a', encoding='utf-8') as file:
        file.writelines(result)

# extract_sentences(input_file_path, output_file_path, input_subject)
extract_sentences(input_file_path, output_file_path)