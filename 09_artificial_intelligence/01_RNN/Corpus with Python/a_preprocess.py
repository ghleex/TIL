import numpy as np
import re


def preprocess(text):
    text = text.lower()
    # text = text.replace('.', ' .')
    # print(text)

    # words = text.split(' ')
    words = re.split('\W', text)
    # print(words)

    word_to_id = {}
    id_to_word = {}

    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word

    # print(word_to_id)
    # print(id_to_word)

    # print(id_to_word[1])
    # print()
    # print(word_to_id['hello'])


    corpus = [word_to_id[w] for w in words]
    corpus = np.array(corpus)
    # print(corpus)

    return corpus, word_to_id, id_to_word

# text = 'You say goodbye and I say hello.'
# print(preprocess(text))
