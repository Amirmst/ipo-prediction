import csv
import pandas as pd

def check(name):
    filters = ['closed', 'highd', 'opend', 'lowd', 'volumed']
    for filter in filters:
        if filter in name:
            return False
    return True

with open('../data.csv', mode='r', encoding='utf-8') as csv_file:
    csvreader = csv.reader(csv_file)
    fields = next(csvreader)
    new_fields = []
    for col in fields:
        if check(col.lower()):
            new_fields.append(col)
            print(col)

    df = pd.read_csv('../data.csv', usecols=new_fields)
    print(df.shape)
    df.to_csv('data_days_removed.csv')

    print(new_fields)
    print(len(new_fields))

