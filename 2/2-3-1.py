file1 = "../popular-names.txt"
file2 = "../col1.txt"
file3 = "../col2.txt"

f2 = open(file2, "w")
f3 = open(file3, "w")

with open(file1, "r") as f1:
    lines = f1.readlines()
    for line in lines:
        print(line)
        col = line.split("\t")
        col1 = col[0]
        f2.write(col1)
        f2.write("\n")
        col2 = col[1]
        f3.write(col2)
        f3.write("\n")