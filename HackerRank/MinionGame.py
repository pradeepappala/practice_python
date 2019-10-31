import re

import re


def minion_game(s):
    length = len(s)
    substrings_s = set([s[i:j] for i in range(length) for j in range(i+1, length+1)])
    kevin_score = stuart_score = 0
    kevin = []
    stuart = []
    for i in substrings_s:
        current_count = len(re.findall('(?=' + i + ')', s))
        if i[0] in 'aeiouAEIOU' :
            kevin_score = kevin_score + current_count
        else:
            stuart_score = stuart_score + current_count

    #print(kevin_score, stuart_score)
    if kevin_score < stuart_score:
        print('Stuart', stuart_score)
    else:
        print('Kevin', stuart_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)
