import csv

rows = 0
with open('data.csv', mode='r', encoding='utf-8') as source_file:
    csvreader = csv.reader(source_file)
    fields = next(csvreader)

    for row in csvreader:
        rows += 1

print(rows)