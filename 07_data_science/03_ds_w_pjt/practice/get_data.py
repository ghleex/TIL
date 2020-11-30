from pprint import pprint
import os
import nltk
import numpy as np
import matplotlib.pyplot as plt
import tensorflow.keras as keras
import sklearn

folder_name = 'inputs'
abs_dir = os.path.join(os.getcwd(), folder_name)
file_names = os.listdir(abs_dir)
file_names = [os.path.join(abs_dir, file_name) for file_name in file_names]

tagged_sentences = nltk.corpus.treebank.tagged_sents()
print('품사 태깅된 문장 수:', len(tagged_sentences))
print(tagged_sentences[0])

sentences, pos_tags = [], []
for tagged_sentence in tagged_sentences:
    sentence, tag_info = zip(*tagged_sentence)
    sentences.append(list(sentence))
    pos_tags.append(list(tag_info))

print(sentences[8])
print(pos_tags[8])

print('샘플의 최대 길이: %d' % max(len(l) for l in sentences))
print('샘플의 평균 길이: %f' % (sum(map(len, sentences)) / len(sentences)))
plt.hist([len(s) for s in sentences], bins=50)
plt.xlabel('length of samples')
plt.ylabel('number of samples')
plt.show()


def tokenize(samples):
    tokenizer = keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(samples)
    return tokenizer


src_tokenizer = tokenize(sentences)
tar_tokenizer = tokenize(pos_tags)

vocab_size = len(src_tokenizer.word_index) + 1
tag_size = len(tar_tokenizer.word_index) + 1
print(f'단어 집합 크기: {vocab_size}')
print(f'태깅 정보 집합 크기: {tag_size}')

X_train = src_tokenizer.texts_to_sequences(sentences)
y_train = tar_tokenizer.texts_to_sequences(pos_tags)
print(X_train[:2])
print(y_train[:2])

max_len = 150
X_train = keras.preprocessing.sequence.pad_sequences(X_train, padding='post', maxlen=max_len)
y_train = keras.preprocessing.sequence.pad_sequences(y_train, padding='post', maxlen=max_len)

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X_train, y_train, test_size=.2, random_state=777)

y_train = keras.utils.to_categorical(y_train, num_classes=tag_size)
y_test = keras.utils.to_categorical(y_test, num_classes=tag_size)

print(f'훈련 샘플 문장 크기: {X_train.shape}')
print(f'훈련 샘플 레이블 크기: {y_train.shape}')
print(f'테스트 샘플 문장 크기: {X_test.shape}')
print(f'테스트 샘플 레이블 크기: {y_test.shape}')
