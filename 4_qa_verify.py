"""

[ GPT4로 생성한 문답지의 유효성 검증 프로세스 ]

< self-instuct 논문의 방법 >
1. 유사성 기반 필터링
ROUGE-L 유사성 체크: 새로 생성된 지시문은 기존 지시문들과의 ROUGE-L 유사성을 기반으로 필터링됩니다. 
유사성 점수가 0.7 미만인 경우에만 새 지시문이 작업 풀에 추가됩니다. 
이는 데이터 세트 내에서의 중복을 최소화하고 다양성을 보장하기 위한 조치입니다.

2. 특정 키워드 필터링
특정 키워드 배제: 언어 모델이 일반적으로 처리하기 어려운 내용을 포함한 지시문은 제외됩니다. 
예를 들어 '이미지', '그림', '그래프' 등과 같은 키워드가 포함된 지시문들은 필터링됩니다.

3. 인스턴스의 중복 및 무효성 검사
완전 중복 제거: 완전히 동일한 인스턴스는 필터링됩니다. 
이는 데이터의 품질을 높이기 위한 중요한 단계입니다.

입력 중복, 출력 다름 제거: 같은 입력에 대해 서로 다른 출력을 가진 인스턴스도 제거됩니다. 이는 일관성과 정확성을 유지하기 위함입니다.
유효성 검사: 유효하지 않은 생성물은 휴리스틱을 기반으로 식별하여 제거됩니다. 예를 들어, 지시문이 너무 길거나 짧거나, 인스턴스 출력이 입력의 단순 반복인 경우가 이에 해당됩니다​​.

< 본 코드의 방법 >
1. 특정 키워드 필터링
2. 질문 중복 제거
3. 200자 이상의 질문, 답변 제거

5_qa_verify_데이터매칭.py 코드

+ 질문&답변이 올바르게 구성됐는지 확인하는 프로세스 (실행 안함)
ip15pro_slidingw_line6.txt 파일에서 6줄 (공백으로 구분) 읽어오고, dataset_qa_ip15pro.txt 에서 3개 세트 가져와서
ip15pro_slidingw_line6.txt 내용에서 dataset_qa_ip15pro.txt가 논리적으로 유도가능한지 확인

self-instruct의 방법이 아니라 현재 제외하였다.

"""


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip().split('\n\n')

def write_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(data))

# 필터링할 키워드 목록
filter_keywords = ['image', 'picture', 'graph']

# 원본 데이터
qa_pairs = read_file('dataset_qa_S23.txt')

verified_pairs = []
excluded_pairs = []
seen_questions = set()

for pair in qa_pairs:
    question, answer = pair.split('\n')
    if any(keyword in question for keyword in filter_keywords):
        reason = f"이유: '{', '.join(filter_keywords)}' 중 하나 이상의 키워드가 질문에 포함됨."
        excluded_pairs.append(pair + "\n" + reason)
    elif question in seen_questions:
        reason = "이유: 동일한 질문의 중복."
        excluded_pairs.append(pair + "\n" + reason)
    elif len(question) > 200 or len(answer) > 200:
        reason = "이유: 질문 또는 답변의 글자수가 200자를 초과함."
        excluded_pairs.append(pair + "\n" + reason)
    else:
        verified_pairs.append(pair)
        seen_questions.add(question)

write_file('dataset_qa_verify_S23.txt', verified_pairs)
write_file('dataset_qa_verify_except_S23.txt', excluded_pairs)
