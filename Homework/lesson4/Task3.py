# 3- Задайте натуральное число N.
#  Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

def list_m(n: int):
    list_n = []
    i = 2
    while n != 1:
        if n % i== 0:
            list_n.append(i)
            n = n // i
        else:
            i += 1
    return list_n

print(set(list_m(12)))                
