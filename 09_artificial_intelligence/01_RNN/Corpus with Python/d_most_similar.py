import numpy as np
from c_02_cos_similarity import preprocess, create_co_matrix, cos_similarity


def most_similar(query, word_to_id, id_to_word, word_matrix, top=5):
    # 검색어 추출
    if query not in word_to_id:
        print(f'{query}(을)를 찾을 수 없습니다.')
        return
    
    print(f'\n[query] {query}')
    query_id = word_to_id[query]
    query_vec = word_matrix[query_id]

    # 코사인 유사도 계산
    vocab_size = len(id_to_word)
    similarity = np.zeros(vocab_size)
    for i in range(vocab_size):
        similarity[i] = cos_similarity(word_matrix[i], query_vec)
    
    # 코사인 유사도를 기준으로 내림차순 출력
    cnt = 0
    for i in (-1 * similarity).argsort():
        if id_to_word[i] == query: continue
        print(f' {id_to_word[i]}: {similarity[i]}')

        cnt += 1
        if cnt >= top: return


text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)
vocab_size = len(word_to_id)
C = create_co_matrix(corpus, vocab_size)

most_similar('you', word_to_id, id_to_word, C, top=5)