string = "パタトクカシーー"
string_list = []

for i in range(0, len(string), 2):
    string_list.append(string[i])

print("".join(string_list))