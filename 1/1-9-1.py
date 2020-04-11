import random

sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

sentence_list = sentence.split(" ")

for word in sentence_list:
    re_word_list = []
    center_chara_list = []
    if len(word) > 4:
        for i in range(len(word)):
            if i == 0 or i == len(word) - 1:
                re_word_list.append(word[i])
            else:
                center_chara_list.append(word[i])
        random.shuffle(center_chara_list)
        center_chara = "".join(center_chara_list)
        re_word_list.insert(1, center_chara)
        re_word = "".join(re_word_list)
        print(re_word)
    else:
        print(word)