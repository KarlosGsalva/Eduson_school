import csv

with open('prices.csv', encoding='UTF-8') as f:
    h, *rows = csv.reader(f, delimiter=';')

goods = [(r[0], h[x], r[x]) for r in rows for x in range(1, len(h))]
cheapest = min(goods, key=lambda x: (int(x[2]), x[1], x[0]))

print(f'{cheapest[1]}: {cheapest[0]}')