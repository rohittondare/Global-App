import csv, json

csvFilePath = 'Names.csv'
#jsonFilePath = 'names.json'

data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows[1]
        data[id] = rows

print(data)