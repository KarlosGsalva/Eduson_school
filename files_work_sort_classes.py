import csv

with open('student_counts.csv', encoding='utf-8', newline='') as file:
    file_dict = csv.DictReader(file)
    colum_list = file_dict.fieldnames
    new_list = ['year'] + sorted(colum_list[1:], key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
    value_list = [[]]
    for i in file_dict:
        for j in new_list:
            value_list[-1].append(i[j])
        value_list.append([])


with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(new_list)
    writer.writerows(value_list)