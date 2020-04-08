string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

string_list = string.split(" ")

word_len_list = []

for word in string_list:
    if word.find(",") != -1 or word.find(".") != -1:
        word_len_list.append(len(word)-1)
    else:
        word_len_list.append(len(word))

print(word_len_list)