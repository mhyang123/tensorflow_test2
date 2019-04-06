from konlpy.tag import Okt
import re
from nltk.tokenize import word_tokenize
#import nltk
#nltk.download()#다운 로그 한고 삭제한다.
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# ***********
# 1 text 문서에서 token 추출하기
# ***********
# Step 1 - pdf 에서 변환한 Document 불러오기
okt = Okt()

ctx = 'C:/Users/ezen/PycharmProjects/test2/data/'
filename = ctx + "kr-Report_2018.txt"
with open(filename, 'r', encoding='utf-8') as f:
    texts = f.read()
print(texts[:300])
texts = texts.replace('/n', ' ')   # 해당줄의 줄바꿈 내용 제거
tokenizer = re.compile('[^ ㄱ-힣]+')   # 한글과 띄어쓰기를 제외한 모든 글자를 선택
texts= tokenizer.sub('', texts)   # 한글과 띄어쓰기를 제외한 모든 부분을 제거
tokens = word_tokenize(texts)
print(texts[:7])
# Step 4 - 복합명사는 묶어서 Filtering 출력
# ex) 삼성전자의 스마트폰은 -- > 삼성전자 스마트폰
noun_token = []
for token in tokens:
    token_pos = okt.pos(token)
    temp      = [txt_tag[0]   for txt_tag in token_pos
                              if txt_tag[1] == 'Noun']
    if len("".join(temp)) > 1:
        noun_token.append("".join(temp))
texts = " ".join(noun_token)
print(texts[:300])


# **************
#불용어 처리
# 2. StopWord 데이터 필터링
# ***************
# stopwords.txt : 2015, 2016, 2017, 2018 모두 출현했던 단어들 불러오기

with open(ctx + "stopwords.txt", 'r', encoding='utf-8') as f:
    stopwords = f.read()
stopwords = stopwords.split(' ')
print(stopwords[:10])

texts = [text for text in tokens if text not in stopwords]
freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)

print(freqtxt[:30])
okt.+('가치창출')
okt.pos('갤러시')#오타는 캘럭시로 처리

wcloud=WordCloud(ctx + "D2Coding.ttf",   relative_scaling = 0.2,
                   background_color = 'white').generate(" ".join(texts))
plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear') #bilinear는 선 모양 이름
plt.axis("off")
plt.show()


