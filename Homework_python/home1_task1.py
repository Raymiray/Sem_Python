# Найдите сумму цифр трехзначного числа n.

# Результат сохраните в перменную res.

n = int(input("Enter a three-digit number: "))

if n>=100 and n<=999:
    firstNum = n//100
    lastNum = n%10
    secondNum = ((n//10)%10)

    res = firstNum + lastNum + secondNum
    print(res)
else:
    print("Error")


# Второй способ
res = 0
while n > 0:
    print(n)
    res += n % 10
    n //= 10
print(res)


# Третий спосбов
# m = int(input())
# sum = 0
# for i in range(len(str(m))):
# sum += m // 10 ** i % 10
# print(sum)


# Четвертый способ
# res = 0
# for i in str(n):
# res+= int(i)



# n1 = n // 100 # Нахождение первой цифры числа
# n2 = (n % 100) // 10 # Нахождение второй цифры числа
# n3 = n % 10 # Нахождение третьей цифры числа
# res = n1 + n2 + n3
# print(res)