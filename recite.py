import os
import sys
import random

def load_word_list(file_name):
    # return [{'word': word, 'mean': mean}, ... ]
    wordlist = []
    fp = open(file_name)
    content = fp.read()
    lines = content.split('\n')
    for line in lines:
        c = line.split('\t')
        c = [i.lstrip().rstrip() for i in c if i.lstrip().rstrip() != '']
        if len(c) == 2:
            word, mean = c
            wordlist.append({'word': word, 'mean': mean})
    return wordlist

def make_schedule(wordlist, daily_new_cnt = 50, need_random = False):
    # for case wordlist: 7, daily_new_cnt : 2
    #[[w1, w2], [w3, w4], [w5, w6], [w7]]
    schedule = []
    if need_random:
        random.shuffle(wordlist)
    while len(wordlist) > 0:
        daily = []
        for i in range(0, daily_new_cnt):
            try:
                daily.append(wordlist.pop(0))
            except IndexError:
                break
        schedule.append(daily)
    return schedule

def make_exam(schedule, current_idx, quiz_count = 100):
    assert(current_idx <= len(schedule))
    quiz_set = []
    for i in range(current_idx):
        quiz_set += schedule[i]
    random.shuffle(quiz_set)
    return quiz_set[0:100]

def test_make_schedule():
    print make_schedule([i for i in range(12)], 10, True)
    print make_schedule([i for i in range(12)], 10, False)

if __name__ == '__main__':
    words = load_word_list('./words.txt')
    print make_schedule(words, 100, True)
