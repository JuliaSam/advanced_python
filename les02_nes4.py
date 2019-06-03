#Реализовать скрипт для преобразования данных в формате csv в формат json;
import csv
import json

csv_file = open('file.csv', 'r')
json_file = open('file.json', 'w')

data = ("name","age","city","job","company")
reader = csv.DictReader(csv_file, data)

for row in reader:
    json.dump(row, json_file)
    json_file.write('\n')