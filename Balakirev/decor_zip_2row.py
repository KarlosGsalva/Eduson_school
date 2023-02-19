def decor_rows(func):
    def wrapper(*args):
        return dict(zip(*func(*args)))
    return wrapper


@decor_rows
def zip_rows(ls1, ls2):
    return ls1.split(), ls2.split()


a = 'house river tree car'
b = 'дом река дерево машина'
d = zip_rows(a, b)
print(*sorted(d.items()))
# result: ('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')
