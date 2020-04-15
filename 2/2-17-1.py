file = "../popular-names.txt"

parson_list = []

with open(file, "r") as f:
    lines = f.readlines()
    for line in lines:
        parson = line.split("\t")[0]
        if parson not in parson_list:
            parson_list.append(parson)

parson_list.sort()

for new_parson in parson_list:
    print(new_parson)