string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

string_list = string.split(" ")

word_dict = {}

for i in range(len(string_list)):
    if i+1 in num_list:
        print(string_list[i][:1])
        word_dict[string_list[i][:1]] = i
    else:
        print(string_list[i][:2])
        word_dict[string_list[i][:2]] = i

print(word_dict)