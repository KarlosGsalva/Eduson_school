def sum_vct(vectors):
    res = [0] * len(vectors[0])
    for vct in vectors:  # вектор
        res = map(sum, zip(res, vct))

    return tuple(res)


vectors = [(1, 2), (3, 4)]
# Ответ: (4, 6)  # Вычисляется как (1 + 3, 2 + 4)
print(sum_vct(vectors))

vectors = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# Ответ: (12, 15, 18)
print(sum_vct(vectors))

print(sum_vct(vectors=[(1, 2), (3, 4), (5, 6)]))
