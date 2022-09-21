import re
import urllib.request
import zipfile
from lxml import etree
from nltk.tokenize import word_tokenize, sent_tokenize


print('Start analysis')

# Data Download
#urllib.request.urlretrieve("https://raw.githubusercontent.com/ukairia777/tensorflow-nlp-tutorial/main/09.%20Word%20Embedding/dataset/ted_en-20160408.xml", filename="../../data/ted_en-20160408.xml")
print('Download seed data :: ../../data/ted_en-20160408.xml')


# Preprocessing
targetXML = open('../../data/ted_en-20160408.xml', 'r', encoding='UTF8')
targetText = etree.parse(targetXML)
print('XML data parsing')

# Delete data except content tag
parseText = '\n'.join(targetText.xpath('//content/text()'))
contentText = re.sub(r'\([^)]*\)', '', parseText)

print('Content loading completed')
print('contentText[:500] = ' + contentText[:500])

print('contentText length = ', len(contentText))

# Sentence tokenize
sentenceText = sent_tokenize(contentText)
print('Sentence tokenize')

# Normalization
from tqdm import tqdm

normalizedText = []
for string in tqdm(sentenceText):
    tokens = re.sub(r'[^a-z0-9]+', ' ', string.lower())
    normalizedText.append(tokens)
print('Normailization')

# Word tokenize
result = [word_tokenize(sentence) for sentence in normalizedText]
print('Word tokenize')

print('Total sample count: {}'.format(len(result)))
for line in result[:3]:
    print(line)

# Word2Vec training
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

model = Word2Vec(sentences = result, vector_size = 100, window=5, min_count=5, workers=4, sg=0)
print('Word2Vec Training complete')

model_result = model.wv.most_similar('man')
print('Most similar \'man\': ')
print(model_result)

# Save Word2Vec models
model.wv.save_word2vec_format('../../resource/eng_w2v')
print('Save Word2Vec : eng_w2v')


