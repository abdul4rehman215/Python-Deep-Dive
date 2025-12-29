# read_file.py
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())
