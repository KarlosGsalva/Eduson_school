def full_err_processing(denom):
    res = ''
    try:
        res += f"Результат: {1/denom}\n"
    except Exception as err:
        res += f"{repr(err)}\n"
    else:
        res += "Ошибок не было!\n"
    finally:
        res += "Главное, все подошло к концу!"
    return res


print(full_err_processing(5))
print(full_err_processing(0))
print(full_err_processing('s'))
