def flat_tuple(tup):
    """method 1"""
    return [i for j in tup for i in j]
#   [элемент for подмассив in исходная_коллекция for элемент in подмассив]
#   2x subarray [el for arr in lst for subarr in arr for el in subarr]

# def flat_tuple(tup):
#     """method 2"""
#     res = []
#     for sub in tup:
#         res.extend(sub)


tup = ([1], [2, '2'], [[1, 2], [3, 4]], [], ['s'])
print(flat_tuple(tup))
