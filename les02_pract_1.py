import csv

prod_field_name = "������������ �������"
name_field_name = "�������� ��"
code_field_name = "��� ��������"
type_field_name = "��� �������"

def get_data(datafile, os_prod_list, os_name_list, os_code_list, os_type_list):
    with open(datafile, encoding='utf-8') as file:
        line = file.readline()
        while len(line) > 0:
            if prod_field_name in line:
                os_prod_list.append(line)
            elif name_field_name in line:
                os_name_list.append(line)
            elif code_field_name in line:
                os_code_list.append(line)
            elif type_field_name in line:
                os_type_list.append(line)
            line = file.readline()
            
datafile_1 = '��������� ��� ������� ��������� �������/info_1.txt'
datafile_2 = '��������� ��� ������� ��������� �������/info_2.txt'
datafile_3 = '��������� ��� ������� ��������� �������/info_3.txt'            

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

get_data(datafile_1, os_prod_list, os_name_list, os_code_list, os_type_list)
get_data(datafile_2, os_prod_list, os_name_list, os_code_list, os_type_list)
get_data(datafile_3, os_prod_list, os_name_list, os_code_list, os_type_list)

main_data = [os_prod_list, os_name_list, os_code_list, os_type_list]

with open ('��������� ��� ������� ��������� �������/os_info.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in main_data:
        writer.writerow(row)
    