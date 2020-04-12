file = "../popular-names.txt"

with open(file, "r") as f:
    lines = f.readlines()
    print(len(lines))