file1 = "../popular-names.txt"
file2 = "../popular-names-11.txt"

f2 = open(file2, "w")

with open(file1, "r") as f1:
    lines = f1.readlines()
    for line in lines:
        print(line)
        replaced_line = line.replace("\t", " ")
        print(replaced_line)
        f2.write(replaced_line)
        f2.write("\n")