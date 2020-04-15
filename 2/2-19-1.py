file = "../popular-names.txt"

parson_dict = {}

with open(file, "r") as f:
    lines = f.readlines()
    for line in lines:
        parson = line.split("\t")[0]
        if parson not in parson_dict:
            parson_dict[parson] = 1
        else:
            parson_dict[parson] += 1

for k, v in sorted(parson_dict.items(), key=lambda x: -x[1]):
    if v > 99:
        print(f" {str(v)} {k}")
    elif v > 9:
        print(f"  {str(v)} {k}")
    else:
        print(f"   {str(v)} {k}")


#print(parson_dict)