# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

sp = [1, 1, 2, 0, -1, 3, 4, 4]
count = 0
b = list()

for c in sp:
    if c not in b:
        b.append(c)
print(len(b))

print(len(set(sp)))
st = set()