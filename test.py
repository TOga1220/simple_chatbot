import csv
from collections import defaultdict


data = defaultdict(int)
print(data)

with open("rank.csv", 'r+') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
        print(row["name"])
        data[row["name"]] = int(row["count"])
        
print(data)