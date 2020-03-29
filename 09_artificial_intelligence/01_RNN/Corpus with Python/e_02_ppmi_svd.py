from e_01_ppmi import preprocess, create_co_matrix, ppmi
from matplotlib import pyplot as plt
import numpy as np


text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)
vocab_size = len(word_to_id)
C = create_co_matrix(corpus, vocab_size, window_size=1)
W = ppmi(C)

# SVD
U, S, V = np.linalg.svd(W)

# 단어 id 가 0 인 단어 벡터 확인
# 동시 발생 행렬
print(f'동시 발생 행렬: {C[0]}')

# PPMI 행렬
print(f'PPMI 행렬: {W[0]}')

# SVD
print(f'SVD: {U[0]}')


# 밀집 벡터의 차원을 2차원 벡터로 감소
print('2차원 벡터')
print(U[0, :2])

# 그래프로 그리기
for word, word_id in word_to_id.items():
    plt.annotate(word, (U[word_id, 1], U[word_id, 0]))

plt.scatter(U[:, 1], U[:, 0], alpha=0.5)
plt.show()

