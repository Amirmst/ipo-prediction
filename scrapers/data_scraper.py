import csv
import requests

stock_symbols = []

API_ENDPOINT = "https://financialmodelingprep.com/api/v3/profile/{fsymbol}?apikey=1df59303d164b13ecff41fe2c9af6ef8"

missing = 0
with open('IPODataFull.csv', mode='r', encoding='latin1') as source_file:
    csvreader = csv.reader(source_file)
    #fields = next(csvreader)

    with open('data-1.csv', mode='a', encoding='utf-8') as dest_file:
        csvwriter = csv.writer(dest_file)
        #fields.append('Description')
        #csvwriter.writerow(fields) 
        for row in csvreader:
            response = requests.get(API_ENDPOINT.format(fsymbol=row[0]))
            response.raise_for_status()
            try:
                description = response.json()[0]['description']
                if description == None or len(description) < 1:
                    missing += 1
                    continue
            except Exception as e:
                missing += 1
                continue

            print(description)
            row.append(description)
            csvwriter.writerow(row)

print("MISSING DATA:", missing)