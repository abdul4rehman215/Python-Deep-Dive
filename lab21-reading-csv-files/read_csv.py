import csv

file_path = "sample.csv"

print("Reading CSV using csv.reader():")
with open(file_path, mode="r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

print("\nSkipping header row:")
with open(file_path, mode="r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        print(row)

print("\nReading CSV using csv.DictReader():")
data_list = []

with open(file_path, mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data_list.append(row)

for item in data_list:
    print(item)
