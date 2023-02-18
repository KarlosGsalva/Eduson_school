
# def sort_dict(d, type, order):
#     """method 1"""
#     nd = {}
#     if order == 'desc' and type == 'keywise':
#         nd = {k: d[k] for k in sorted(d.keys(), reverse=True)}
#     elif order == 'desc' and type == 'valuewise':
#         nd = {k[0]: k[1] for k in sorted(d.items(), key=lambda x: x[1], reverse=True)}
#     elif order == 'asc' and type == 'keywise':
#         nd = {k: d[k] for k in sorted(d.keys())}
#     elif order == 'asc' and type == 'valuewise':
#         nd = {k[0]: k[1] for k in sorted(d.items(), key=lambda x: x[1])}
#     return nd


def sort_dict(d, type, order):
    """method 2"""
    if type == "keywise":
        idx = 0
    else:
        idx = 1

    if order == "desc":
        reverse = True
    else:
        reverse = False

    return dict(sorted(d.items(), key=lambda x: x[idx], reverse=reverse))

d = {'a': 1, 'b': 5, 'c': 0}
type = 'keywise'
order = 'desc'
print(sort_dict(d, type, order))
# {
#     'c': 0,
#     'b': 5,
#     'a': 1
# }

d = {'a': 1, 'b': 5, 'c': 0}
type = 'valuewise'
order = 'desc'
print(sort_dict(d, type, order))
# {
#     'b': 5,
#     'a': 1,
#     'c': 0
# }

d = {'a': 1, 'b': 5, 'c': 0}
type = 'keywise'
order = 'asc'
print(sort_dict(d, type, order))
# {
#     'a': 1,
#     'b': 5,
#     'c': 0
# }

d = {'a': 1, 'b': 5, 'c': 0}
type = 'valuewise'
order = 'asc'
print(sort_dict(d, type, order))
# {
#     'c': 0,
#     'a': 1,
#     'b': 5
# }
