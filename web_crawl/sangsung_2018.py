from konlpy.tag import Okt
import re
from nltk.tokenize import word_tokenize
import nltk
nltk.download()#다운 로그 한고 삭제한다.

#okt = Okt()
# ***********
# 1 text 문서에서 token 추출하기
# ***********

# Step 1 - pdf 에서 변환한 Document 불러오기
ctx = 'C: /Users/ezen/PycharmProjects/test2/data/'
filename = ctx + "kr-Report_2018.txt"

with open(filename, 'r', encoding='utf-8') as f:

    texts = f.read()

print(texts[:300])

texts = texts.replace('/n', ' ')   # 해당줄의 줄바꿈 내용 제거

tokenizer = re.compile('[^ ㄱ-힣]+')   # 한글과 띄어쓰기를 제외한 모든 글자를 선택

texts= tokenizer.sub('', texts)   # 한글과 띄어쓰기를 제외한 모든 부분을 제거

tokens = word_tokenize(texts)
print(texts[:7])