#����������� ������ ��� ������/������ ������ � ������� json;

import json

dict = {
    "name": "Julia",
    "age": 28,
    "city": "Novosibirsk",
    "job": "Analyst",
    "company": "2GIS"
       }
#��� ������
with open ('dict_json', 'w') as file:
    json.dump(dict, file)
    
#��� ������
with open ('dict_json') as file:
    print(file.read())