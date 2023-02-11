import csv


def key_func(grade):
    number, letter = grade.split('-')
    return int(number), letter


with open('student_counts.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    colums = ['year'] + sorted(reader.fieldnames[1:], key=key_func)
    rows = list(reader)


with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as w_file:
    writer = csv.DictWriter(w_file, fieldnames=colums)
    writer.writeheader()
    writer.writerows(rows)

