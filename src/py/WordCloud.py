from collections import Counter  # 단어 카운트 라이브러리
from wordcloud import WordCloud  # 워드클라우드 라이브러리
from konlpy.tag import Okt       # 트위터 기반 한국어 형태소 분석기 || 이외에도 오픈 라이브러리로 제공되는 Hannanum, kkma, Komoran, Mecab 등이 있음
import nltk                      # nltk 라이브러리

def wordcloud_from_text(input_file, output_file='wordcloud.png', method=0):
    # get text from file
    try:
        with open(input_file, 'rb') as f:
            text = f.read().decode('utf-8')
    except Exception as e:
        print('wordcloud_from_text() - %s' %(e))
        return
    
    # 예외처리
    if text == None:
        print('wordcloud_from_text() text is None')
        return

    # 명사구 추출
    print('Extract Noun Phrase...')
    noun_list = get_noun_list(text, method)
    
    # 예외처리 2
    if len(noun_list) < 10:
        print('wordcloud_from_text() - Too small noun list')
        return
    
    # 워드 클라우드 생성
    print('To make word cloud...')
    wc = WordCloud(font_path = '../resource/D2Coding-Ver1.3.2-20180524-ligature.ttf',
                       background_color = 'black',
                       width=512, height=512,
                       max_font_size=500,
                       max_words=1000)
    wc.generate_from_frequencies(dict(noun_list))
    wc.to_file(output_file)
    print('Create WordCloud:', output_file)

def get_noun_list(text, method=0):
    # Sentence to token
    if method == 0:
        # 한국어
        noun = tokenizer_konlpy(text)
    else :
        # 영어
        noun = tokenizer_nltk(text)
    
    # Count word
    count = Counter(noun)
    
    # Get most frequent words
    noun_list = count.most_common(200)
    return noun_list

def tokenizer_nltk(text): # 영어
    
    is_noun = lambda pos : (pos[:2] == 'NN' or pos[:2] == 'NNP')
    tokenized = nltk.word_tokenize(text)
    
    print('   Tokenize and pos tagging')
    return [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

def tokenizer_konlpy(text): # 한글
    okt = Okt()
    print('   Tokenize and pos tagging')
    return [word for word in okt.nouns(text) if len(word) > 1 ]

