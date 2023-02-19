t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
     ' ': '-', '"': '-', ':': '-', ';': '-', '.': '-', ',': '-', '_': '-', '-': '-'}


# здесь продолжайте программу
def decorator(function):
    def wrapper(text):
        message = function(text)
        while '--' in message:
            message = message.replace('--', '-')
        return message
    return wrapper


@decorator
def converter(text):
    result = []
    for char in text:
        if char in t:
            result.append(t[char])
        else:
            result.append(char)

    return ''.join(result)


s = input().lower()
print(converter(s))
# Sample Input:
#
#     Python - это круто!
# Sample Output:
#
#     python-eto-kruto!
