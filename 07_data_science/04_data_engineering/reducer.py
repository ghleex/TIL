import sys

cur_word = None
cur_cnt = 0
word = None

for line in sys.stdin:
    line = line.strip()

    word, cnt = line.split('\t', 1)

    try:
        cnt = int(cnt)
    except ValueError:
        continue

    if cur_word == word:
        cur_cnt += cnt
    else:
        if cur_word:
            print('%s\t%s' % (cur_word, cur_cnt))
        
        cur_cnt = cnt
        cur_word = word

if cur_word == word:
    print('%s\t%s' % (cur_word, cur_cnt))


# cat input.txt | python mapper.py | sort -k 1
# cat input.txt | python mapper.py | sort -k1,1 | python reducer.py | sort -k 2 -r
