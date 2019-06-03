#Реализовать скрипт для чтения/записи данных в формате json;

import json

dict = {
    "name": "Julia",
    "age": 28,
    "city": "Novosibirsk",
    "job": "Analyst",
    "company": "2GIS"
       }
#для записи
with open ('dict_json', 'w') as file:
    json.dump(dict, file)
    
#для чтения
with open ('dict_json') as file:
    print(file.read())