import re


def rebuild_string(s):
    if s[:2] == '+7' or s[:2] == '+8':
        s = s[2:].replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    else:
        s = s[1:].replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    return f'+7({s[:3]}){s[3:6]}-{s[6:]}'


def rgx_phn(phones):
    res_p = []
    for i in phones:
        res_p.append(i if re.search('[+78][ ()-]\d{3}[ ()-]\d{3}[ ()-]\d{4}\\b|'
                                    '[+78][ ()-]\d{3}[ ()-]\d{3}[ ()-]\d{2}[ ()-]\d{2}\\b|'
                                    '[+78][ ()-]\d{4}[ ()-]\d{3}[ ()-]\d{3}\\b|'
                                    '\d{10}', i) else -1)
    res = []
    for i in res_p:
        if i != -1:
            res.append(rebuild_string(i))
        else:
            res.append(i)
    return res

# tests
# phones = ['+7(123)456-7890', '81234567890', '+7 123 456 78901', '123 456 7890']
# phones = ['+7(123)456-7890', '+8(123)456-7890', '7(123)456-7890', '8(123)456-7890', '+7 123 456-7890', '+7 123 456-78-90', '+7-123-456-78-90', '+7(1234)567-890', '+7 123 456 7890', '+7 123 456 789', '+7 123 456 78901', '+123 456 78901']
