import sys

lines_amount = int(sys.argv[1])

file = "../popular-names.txt"

i = 1

with open(file, "r") as f:
    lines = f.readlines()
    for line in lines:
        if i < len(lines) - lines_amount + 1:
            i += 1
            continue
        else:
            print(line.replace("\n", ""))
            i += 1