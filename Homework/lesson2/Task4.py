#4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
#не использовать random.randint и вообще библиотеку random
#Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

import random

def get_list(n, lft, rght):
    return [random.randint(lft, rght) for i in range(n)]

def shuffle_list(lst):
    return random.shuffle(lst)

n = 10
lft = -20
rght = 50

mylist = get_list(n, lft, rght)
print(mylist)
shuffle_list(mylist)
print(mylist)