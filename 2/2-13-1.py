file1 = "../col1.txt"
file2 = "../col2.txt"
file3 = "../popular-names.txt"
file4 = "../marge-13.txt"


def file_open(file):
    with open(file, "r") as f:
        lines = f.readlines()
    return lines


f1_lines = file_open(file1)
f2_lines = file_open(file2)

f4 = open(file4, "w")

for i in range(len(f1_lines)):
    f1_line = f1_lines[i].replace("\n", "")
    f2_line = f2_lines[i].replace("\n", "")
    f4.write(f1_line)
    f4.write("\t")
    f4.write(f2_line)
    f4.write("\n")