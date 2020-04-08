string1 = "パトカー"
string2 = "タクシー"
string_list = []

for i in range(len(string1)):
    string_list.append(string1[i])
    string_list.append(string2[i])

print("".join(string_list))