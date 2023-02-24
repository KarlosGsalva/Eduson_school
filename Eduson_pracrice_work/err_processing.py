def err_processing(d):
    try:
        res = 1/d.get('denom')
        # ваше решение ниже
    except ZeroDivisionError as res:
        return f'Деление на 0 запрещено! Ошибка: {repr(res)}.'
    except TypeError as res:
        return f'Проверьте переданный тип denom! Ошибка: {repr(res)}.'
    except Exception as res:
        return f'Непредвиденная ошибка: {repr(res)}.'
    else:
        return res


print(err_processing({'denom': 2}))
# 0.5
print(err_processing({'denom': 's'}))
# Проверьте переданный тип denom! Ошибка: TypeError("unsupported operand type(s) for /: 'int' and 'str'").
print(err_processing({'denom': 0}))
# Деление на 0 запрещено! Ошибка: ZeroDivisionError('division by zero').
print(err_processing(1))
# Непредвиденная ошибка: AttributeError("'int' object has no attribute 'get'").
