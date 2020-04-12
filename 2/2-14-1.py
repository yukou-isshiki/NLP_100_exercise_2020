import sys

lines_amount = int(sys.argv[1])

file = "../popular-names.txt"

with open(file, "r") as f:
    lines = f.readlines()
    i = 1
    for line in lines:
        if i > lines_amount:
            break
        else:
            print(line.replace("\n", ""))
            i += 1