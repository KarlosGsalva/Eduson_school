import re


# def rebuild_string(s):
#     if s[0] == '+':
#         s = s[2:]
#     else:
#         s = s[1:]
#     s = s.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
#     return f'+7({s[:3]}){s[3:6]}-{s[6:]}'
#
#
# def rgx_phn(phones):
#     res_p = []
#     for i in phones:
#         res_p.append(i if re.search('[+78][ ()-]\d{3}[ ()-]\d{3}[ ()-]\d{4}\\b|'
#                                     '[+78][ ()-]\d{3}[ ()-]\d{3}[ ()-]\d{2}[ ()-]\d{2}\\b|'
#                                     '[+78][ ()-]\d{4}[ ()-]\d{3}[ ()-]\d{3}\\b|'
#                                     '\d{10}', i) else -1)
#     res = []
#     for i in res_p:
#         if i != -1:
#             res.append(rebuild_string(i))
#         else:
#             res.append(i)
#     return res

# tests
# phones = ['+7(123)456-7890', '81234567890', '+7 123 456 78901', '123 456 7890']
phones = ['+7(123)456-7890', '+8(123)456-7890', '7(123)456-7890', '8(123)456-7890', '+7 123 456-7890', '+7 123 456-78-90', '+7-123-456-78-90', '+7(1234)567-890', '+7 123 456 7890', '+7 123 456 789', '+7 123 456 78901', '+123 456 78901']



def rgx_phn(phones):

    if phones is None:
        raise AttributeError('An attribute should not be None')

    res = []

    trim = re.compile(r'(?:^\+?|[()\s-]*)')

    check = re.compile(r'(?:7|8)([0-9]{3})([0-9]{3})([0-9]{4})')

    for i in phones:
        t = trim.sub('', i)
        c = check.match(t)
        if (len(t) == 11 and c):
            res.append(f'+7({c[1]}){c[2]}-{c[3]}')
        else:
            res.append(-1)

    return res


print(rgx_phn(phones))