def dec_list(func):
    def wrapper(lst_1):
        return sorted(func(lst_1))
    return wrapper


@dec_list
def get_list(lst_1):
    return list(map(int, lst_1.split()))


lst = get_list(input())
print(*lst)
