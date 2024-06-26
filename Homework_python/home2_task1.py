# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. 
# Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.
# Входные данные:

# На вход программе подается список coins, где coins[i] равно 0, 
# если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

# Выходные данные:
# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
# Пример использования На входе:

coins = [1, 1, 0, 1, 1, 0]
o = 0
r = 0

for i in range(len(coins)):
    if coins[i] == 1:
        r += 1
    else:
        o += 1

if o > r:
    print(r)
else:
    print(o)
