# The Arcane Odyssey

import cowsay
import random

def Main_Game_Func(total_coins, death_cost, helper):
    while True:
        if total_coins <= 0:
            return

        helper += 1

        if helper % 10 == 0:
            death_cost += 25

        position_of_rock = random.randint(1, 3)

        cowsay.tux('Muhaha')
        print(f'\n'      '\n'      '')
        position = input(f'Type the position you are thinking it is going to throw "mid", "left" or "right" ==> ')

        if dict_helper[position] == position_of_rock:
            print(f'\n'      '\n'      '')
            print(f'Nice! You are + 100 coins!')
            total_coins += 100
        else:
            print(f'\n'      '\n'      '')
            print(f'Ahh! Mate you just lost {death_cost}')
            total_coins -= 50

        print(f'\n'      '\n'      '')

        while True:
            print(f'Options:')
            print(f'If you want to fight type "Ready"')
            print(f'if you wanna browse some items then type "Open store"')
            print(f'if you want to check you gear type "Gear"')
            answer = input(f'>>> ')

            if answer.lower() == 'ready':
                break
            elif answer.lower() == 'open store':
                Store_Func(total_coins)

            elif answer.lower() == 'gear':
                Gear_Func()
                continue
            else:
                print(f'Error')
                print(f'Try again!')
                print(f'\n'      '\n'      '')
                continue


def Store_Func(total_coins):
    print(f'\n'      '\n'      '')
    print(f'You have {total_coins} coins')
    print(f'Here are all of the store offerts:')

    for i, x in store_items.items():
        print(f'{i} - {x[0]}, {x[1]}, {x[2]}')
    print(f'\n'      '')

    while True:

        print(f'If you wanna buy an item type the name of the item or if you don\'t want just type "exit"')
        answer = input('>>> ')

        if answer.lower() == 'exit':
            print(f'Good luck in the next fight!')
            print(f'\n'      '\n'      '')
            break
        else:
            for i in store_items.keys():
                if answer == i and store_items[i][2] == 'Unowned':
                    if total_coins - 1 >= store_items[i][0]:
                        store_items[i][2] = 'Owned'
                        for x in body_items.keys():
                            if store_items[i][1] == x:
                                body_items[x] = i
                                total_coins -= store_items[i][0]
                                print(f'You just bought {body_items[x]}!')
                                print(f'\n'      '')
                                break
                        break
                    else:
                        if total_coins - store_items[answer][0] == 0:
                            print(f'If you buy it you will have 0 coins!!!')
                            print(f'\n'      '\n'      '')
                            break
                        print(f'Not enough money!')
                        print(f'\n'      '\n'      '')
                        break
                else:
                    continue

def Gear_Func():
    print(f'\n'      '')
    print(f'That is your gear {name}:')
    for i in body_items.keys():
        print(f'{i} => {body_items[i]}')
    print(f'\n'      '')
    print(f'Ready to continue?')
    answer = input(f'>>> ')
    print(f'\n'      '\n'      '')



# The Arcane Odyssey

print(f'Welcome to "The Arcane Odyssey" player!')
print(f'Can you help our team to defeat the big monster?')
answer = input(f'>>> ')

total_coins = 300
death_cost = 50
helper = 0

dict_helper = {'mid': 1, 'left': 2, 'right': 3}
store_items = {'Cheese Bowl': [300, 'Helmet', 'Unowned'], 'Cheese Protector': [500, 'Chest', 'Unowned'], 'Cheese Farters': [400, 'Legs', 'Unowned'],
               'Cheese Socks': [250, 'Feet', 'Unowned'], 'Ghost Defender': [125, 'Shield', 'Unowned'], 'Stone Cutter': [100, 'Weapon', 'Unowned']}
body_items = {'Helmet': 'None', 'Chest': 'None', 'Legs': 'None', 'Feet': 'None', 'Shield': 'Default', 'Weapon': 'Default'}
backpack = {}

name = input(f'Before we start can you enter your name? ==> ')

print(f'Ok, let\'s begin!')

print('\n'      '\n'      '')



answer = input(f'Type in "Ready" if you are ==> ')
print(f'I doesn\'t matter what you say we are starting!')
print(f'\n'      '\n'      '')
print(f'The monster is strong and you need to predict where it is going to throw a rock!')
print(f'You need to type the position you think the rock will fall if you don\'t guess it correctly you are loosing {death_cost} coins!')
print(f'Every 10th round you will loose with 25 more coins.')
print(f'Just a reminder that you have {total_coins} coins.')
print(f'Good luck!')

Main_Game_Func(total_coins, death_cost, helper)
