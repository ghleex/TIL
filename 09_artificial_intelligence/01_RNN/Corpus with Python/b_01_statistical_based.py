import numpy as np
from a_preprocess import preprocess

text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)

# print(corpus)

# print(id_to_word)

C = np.array([
    [0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
], dtype=np.int32)

# ID 가 0 인 벡터 표현
print(C[0])

# ID 가 4 인 벡터 표현
print(C[4])

# "goodbye" 의 벡터 표현
print(C[word_to_id['goodbye']])
