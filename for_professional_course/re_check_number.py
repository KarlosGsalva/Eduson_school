import re
import time

start = time.perf_counter()
text = 'Перезвони мне, пожалуйста: 7-919-667-21-19'
patterns = [r'7-\d{3}-\d{3}-\d{2}-\d{2}', r'8-\d{3}-\d{4}-\d{4}']
for i in patterns:
    [print(j) for j in re.findall(i, text)]

print(time.perf_counter() - start)

start = time.perf_counter()
patterns = r'7-\d{3}-\d{3}-\d{2}-\d{2}|8-\d{3}-\d{4}-\d{4}'
[print(i) for i in re.findall(patterns, text)]

print(time.perf_counter() - start)

# "Перезвони мне, пожалуйста: 7-919-667-21-19"
# "Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911"

# 7-919-667-21-19
# 0.00018259999342262745

# 7-919-667-21-19
# 0.00011449999874457717

# 7-919-667-21-19
# 8-917-4864-1911
# 0.00020220001169946045

# 7-919-667-21-19
# 8-917-4864-1911
# 0.00012149999383836985
