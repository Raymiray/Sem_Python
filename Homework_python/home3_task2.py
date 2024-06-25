# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [1, 12, 6, 7, 8, 15]
k = 11
# 5
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)

# Второй вариант
list_1 = [1, 2, 3, 4, 0, 5]
k = -5

# Введите ваше решение ниже
index = 0
i = k-1
j = k+1

while index < len(list_1):
    if k in list_1:
        print(k)
        break
    else:
        if i in list_1 and j in list_1:
            print(i,j)
            break
        elif i in list_1 and j not in list_1:
            print(i)
            break
        elif i not in list_1 and j in list_1:
            print(j)
            break
        else:
            i-=1
            j+=1
    index+=1