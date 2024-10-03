
'''

[ 슬라이딩 윈도우로 분할한 데이터를 원본 데이터와 매칭 ]

'''

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip().split('\n\n')

sliding_window_data = read_file('ip15pro_slidingw_line6.txt')
qa_data = read_file('dataset_qa_ip15pro.txt')

for i in range(78):

    sliding_window_chunk = sliding_window_data[i]
    
    qa_pairs_chunk = qa_data[i*3:(i+1)*3]
    qa_pairs = ['\n'.join(pair.split('\n')) for pair in qa_pairs_chunk]
    
 
    print("Sliding Window Chunk:")
    print(sliding_window_chunk)
    print("\nQ&A Pairs:")

    print(qa_pairs[0] + "\n")
    print(qa_pairs[1] + "\n")
    print(qa_pairs[2] + "\n")

    print("\n" + "-"*50 + "\n")