# Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

n = [1, 2, 3, 4, 5]

k = int(input("Enter a number: "))
k = k%len(n)
for i in range(k):
    t = n.pop()
    n.insert(0,t)
print(n)