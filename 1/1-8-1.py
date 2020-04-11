def cipher(sentence):
    chara_list = []
    for i in range(len(sentence)):
        if sentence[i].islower() == True:
            convert_chara = chr(219 - ord(sentence[i]))
            chara_list.append(convert_chara)
        else:
            chara_list.append(sentence[i])
    reverse_sentence = "".join(chara_list)
    return reverse_sentence

def recipher(sentence):
    chara_list = []
    for i in range(len(sentence)):
        if reverse_sentence[i].islower() == True:
            re_chara = chr(219 - ord(sentence[i]))
            chara_list.append(re_chara)
        else:
            chara_list.append(sentence[i])
    re_sentence = "".join(chara_list)
    return re_sentence


if __name__ == '__main__':
    sentence = ""
    reverse_sentence = cipher(sentence)
    print(reverse_sentence)
    resentence = recipher(reverse_sentence)
    print(resentence)