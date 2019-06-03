#Реализовать скрипт для чтения/записи данных в формате yaml;
import yaml
dict = {
    "name": "Julia",
    "age": 28,
    "city": "Novosibirsk",
    "job": "Analyst",
    "company": "2GIS"
       }

with open('write.yaml','w') as file: 
    yaml.dump(dict, file)

with open('write.yaml') as file:
    print(file.read())