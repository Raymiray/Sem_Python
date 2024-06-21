dikt1 = {333: 2, (1,2): 3, "qwerty":[1,2]} #ключи только неизменяемые значения
print(dikt1)

for i in dikt1:
    print(i, dikt1[i])

for i in dikt1.values():
    print(i)

for i,j in dikt1.items():
    print(i,j)
