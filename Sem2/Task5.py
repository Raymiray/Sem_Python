# Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – 
# соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число
# 0
# 0.

# Тестовые данные 🟢
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31

# Первое решение
n = 'ООООООРРРОРОРРРРРРР'
o = 0
om = 0
p = 0
pm = 0
for i in n:
    if i == 'О':
        o += 1
        om = o
        p = 0
    elif i == 'Р':
        p += 1
        pm = p
        o = 0

print(max(om, pm))


# Второе решение
import random

num_try = int(input("Введите количеств бросков монеток = "))

string = ""
for i in range(num_try):
    string += random.choice(["Р","О"])

print(string)

max = 0
count = 1
i = 0

while "Р" * i in string:
    i += 1
print(i - 1)
print("Р" not in ["Р","О"])