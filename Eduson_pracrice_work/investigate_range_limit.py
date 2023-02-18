def segment(num, scale):
    """method1"""
    n_left = max(i for i in scale if i <= num)
    n_right = min(i for i in scale if i >= num)
    res = n_left, n_right
    return res


# def segment(num, scale):
#     """method2"""
#     # при len(scale) == 1 склеенный со сдвигом список будет пустым
#     if num == scale[0]:
#         return (num, num)
#
#     for n1, n2 in zip(scale, scale[1:]):
#         if n1 < num < n2:
#             return (n1, n2)
#         elif num == n2:
#             return (n2, n2)
#
#     # В идеале не должно выполниться
#     return 'Ошибка в алгоритме'

# def segment(num, scale):
#     """method3"""
#     # на случай единственного элемента в списке
#     if num == scale[0]:
#         return (num, num)
#
#     # работает медленно
#     for i in range(len(scale)-1):
#         n1 = scale[i]
#         n2 = scale[i+1]
#         if n1 < num < n2:
#             return (n1, n2)
#         elif num == n2:
#             return (n2, n2)
#
#     # В идеале не должно выполниться
#     return 'Ошибка в алгоритме'

# def segment(num, scale):
#     """method4"""
#     n1 = None
#     # работает медленно
#     while scale:
#         n2 = scale.pop(0)
#         if n2 == num:
#             return (n2, n2)
#         elif n1 is not None:
#             if n1 < num < n2:
#                 return (n1, n2)
#         n1 = n2
#
#     # В идеале не должно выполниться
#     return 'Ошибка в алгоритме'


"""test1"""
scale_list = [10, 20, 30, 40, 50]
number = 30
print(segment(number, scale_list))

"""test2"""
scale_list = [10, 20, 30, 40, 50]
number = 30
print(segment(number, scale_list))

