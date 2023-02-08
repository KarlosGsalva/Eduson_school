def show_menu(func):
    def wrapper(words):
        [print(f'{i}. {j}') for i, j in enumerate(func(words), start=1)]
    return wrapper


@show_menu
def get_menu(words):
    return words.split()
