from functools import reduce


def find_max(arr):
    # ваше решение ниже
    return reduce(lambda x, y: x if x > y else y, arr) if arr else None


# def find_max(arr):
#     return reduce(lambda x, y: x if x>y else y, arr if arr else [None])


arr = [1, 20, -3, 5, 0]
print(find_max(arr))