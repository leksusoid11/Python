# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Тот, кто берет последнюю конфету - проиграл.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""




# вариант человек против бота:
from random import randint, choice

greeting = ('Здравствуйте! Это игра "Забери все конфеты!" Начинаем нашу игру')

messages = [
    "Ваша очередь брать конфеты",
    "возьмите конфеты",
    "сколько конфет возьмёте?",
    "берите, не стесняйтесь",
    "Ваш ход",
]


def introduce_players():
    player1 = input("Давайте знакомиться. Как Вас зовут?\n")
    player2 = "Олег"
    print(f"Очень приятно, меня зовут {player2}")
    return [player1, player2]


def get_rules(players):
    n = int(input("Сколько конфет будем разыгрывать?\n "))
    m = int(input("Сколько максимально будем брать конфет за один ход?\n "))
    first = int(input(f"{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n"))
    if first != 1:
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    print(count)
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = "а"
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = "ы"
    else:
        letter = ""
    while rules[0] > 0:
        if not count % 2:
            move = rules[0] % rules[1] + 1
            print(f"Я забираю {move}")
        else:
            print(f"{players[0]}, {choice(messages)}")
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(f"Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}")
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f"Попробуйте ещё раз, у Вас {attempt} попытки")
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f"Очень жаль, у Вас не осталось попыток. Game over!")
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f"Осталось {rules[0]} конфет{letter}")
        else:
            print("Все конфеты разобраны.")
        count += 1
    return players[not count % 2]


print(greeting)

players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print("У нас нет победителя.")
else:
    print(f"Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!")


    # вариант человек против бота c "интеллектом":
# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


# def bot_calc(value):
#     k = randint(1,29)
#     while value-k <= 28 and value > 29:
#         k = randint(1,29)
#     return k

# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = bot_calc(value)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")