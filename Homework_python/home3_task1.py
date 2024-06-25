# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
list_1 = [1, 2, 3, 4, 5]
k = 3
# 1
count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)


# Второй способ
from array import array

n = int(input('Введите количество чисел: '))
if n <= 0:
    print('Число не положительное')
    exit()
data = array('i')
for i in range(n):
    data.append(int(input('Введите число № {}: '.format(i + 1))))
x = int(input('Введите число для поиска: '))

count = data.count(x)
print(count)