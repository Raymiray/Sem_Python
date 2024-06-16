# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.


#МОЕ РЕШЕНИЕ
# n = 385916

# firstNumber = n//1000
# secondNumber = n%1000

# firstDig = firstNumber//100
# secondDig = ((firstNumber//10)%10)
# lastDig = firstNumber%10

# firstDig2 = secondNumber//100
# secondDig2 = ((secondNumber//10)%10)
# lastDig2 = secondNumber%10

# res = firstDig + secondDig + lastDig
# res2 = firstDig2 + secondDig2 + lastDig2

# if res == res2:
#     print("yes")
# else:
#     print("no")

n = 385916
# counts = len(str(n)) - не нужна

res1 = 0
res2 = 0

for i in str(n):
    if n >= 1000:
        res2 += n % 10
        n = n // 10
    else:
        res1 += n % 10
        n = n // 10

if res1 == res2:
    print("yes")
else:
    print("no")