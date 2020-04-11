def figure_n_gram(sentence):
    n_gram_list = []
    for i in range(len(sentence)):
        if i == len(sentence) - 1:
            continue
        else:
            n_gram_list.append(f"{sentence[i]}{sentence[i+1]}")
    return n_gram_list

def contain_part(part, list):
    if part in list:
        return True
    else:
        return False


if __name__ == '__main__':
    sentence1 = "paraparaparadise"
    sentence2 = "paragraph"
    x = figure_n_gram(sentence1)
    y = figure_n_gram(sentence2)
    x_or_y = set(x+y)
    x_and_y = set(x).intersection(y)
    only_x_or_only_y = x_or_y - x_and_y
    print(x_or_y)
    print(only_x_or_only_y)
    print(x_and_y)
    x_result = contain_part("se", x)
    y_result = contain_part("se", y)
    print(x_result)
    print(y_result)