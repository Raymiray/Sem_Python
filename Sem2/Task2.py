# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a = int(input("Enter a number: "))

num1 = 0
num2 = 1
num3 = 0
count = 2

while a > num3:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    count +=1
    if num3 > a:
        count = -1
print(count)
    


