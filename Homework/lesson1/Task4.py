# 4-Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


from random import randint

x = randint (-100, 100)
y = randint (-100, 100)

def get_quarter_number (x, y):
    if x != 0 and y != 0:
        if x * y > 0:
            if x > 0: return 1
            else: return 3
        else:
            if x < 0: return 2
            else: return 4
    else: 
        if x == 0: return 'OY'
        else: return 'OX'
    
print (f'Точка: {x, y}')
print (f'Четверть: {get_quarter_number(x, y)}')
