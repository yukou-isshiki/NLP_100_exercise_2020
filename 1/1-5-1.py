def word_n_gram(sentence):
    sentence_list = sentence.split(" ")
    for word in sentence_list:
        if len(word) < 3:
            print(word)
        else:
            figure_n_gram(word)


def figure_n_gram(sentence):
    for i in range(len(sentence)):
        if i == len(sentence) - 1:
            continue
        else:
            print(f"{sentence[i]}{sentence[i+1]}")



if __name__ == '__main__':
    sentence = "I am an NLPer"
    word_n_gram(sentence)
    figure_n_gram(sentence)