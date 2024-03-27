# The Arcane Odyssey
# Importing libraries
import cowsay
import random

# Creating a func for the main game logic
def Main_Game_Func(total_coins, death_cost, round, level, xp, xp_to_lvl_up, coin_boost_active, wins, looses):
    while True:

        # Adding 1 round
        round += 1

        # Every 10 rounds the death tax increases
        if round % 10 == 0:
            death_cost += 25

        # Picking random possition
        position_of_rock = random.randint(1, 3)

        cowsay.tux('Muhaha')
        print(f'\n'      '\n'      '')
        position = input(f'Type the position you are thinking it is going to throw "mid", "left" or "right" ==> ')

        # Chek if you guesssed corectly 
        if dict_helper[position] == position_of_rock:
            # Chek if you have bought the coin booster from the shop
            if coin_boost_active:
                print(f'\n'      '\n'      '')
                print(f'Nice! You are + 150 coins!')
                total_coins += 150
                wins += 1
                coin_boost_active = False
            else:
                print(f'\n'      '\n'      '')
                print(f'Nice! You are + 100 coins!')
                total_coins += 100
                wins += 1
            xp += 10
            # Chek id you have enough xp to level up
            if xp >= xp_to_lvl_up:
                level += 1
                xp -= xp_to_lvl_up
                xp_to_lvl_up += 20
                # Every 5th level the program prints the level
                if level % 5 == 0:
                    print(f'\n'      '')
                    print(f'Reach Level {level}')

        # If you havent guess the possition right
        else:
            print(f'\n'      '\n'      '')
            print(f'Ahh! Mate you just lost {death_cost}')
            total_coins -= 50
            looses += 1
            coin_boost_active = False
            # Chek if you are out of coins
            if total_coins <= 0:
                print(f'Game over!')
                Stats_Func(round, wins, looses, level, total_coins, death_cost)
                return

        print(f'\n'      '')

        # While for menu options
        while True:
            print(f'Options:')
            print(f'If you want to fight type "Ready"')
            print(f'If you wanna browse some items then type "Open store"')
            print(f'If you want to check you gear type "Gear"')
            print(f'If you want to see your stats type "Stats"')
            answer = input(f'>>> ')

            # Check what is the choosen option
            if answer.lower() == 'ready':
                break
            elif answer.lower() == 'open store':
                Store_Func(total_coins, coin_boost_active)

            elif answer.lower() == 'gear':
                Gear_Func()
                continue
            elif answer.lower() == 'stats':
                Stats_Func(round, wins, looses, level, total_coins, death_cost)
            else:
                print(f'Error')
                print(f'Try again!')
                print(f'\n'      '\n'      '')
                continue

# Store logic
def Store_Func(total_coins, coin_boost_active):
    print(f'\n'      '\n'      '')
    print(f'You have {total_coins} coins')
    print(f'Here are all of the store offerts:')

    # Printing all the items
    for i, x in store_items.items():
        if i == 'Coin Booster':
            print(f'{i} - {x[0]}, {x[1]}')
            continue
        print(f'{i} - {x[0]}, {x[1]}, {x[2]}')
    print(f'\n'      '')

    # While for buying items or coin booster
    while True:

        print(f'If you wanna buy an item type the name of the item or if you don\'t want just type "exit"')
        answer = input('>>> ')

        if answer.lower() == 'exit':
            print(f'Good luck in the next fight!')
            print(f'\n'      '\n'      '')
            break
        else:
            for i in store_items.keys():
                # 'Coin Booster': 'Boosts the win from the next match with 50%'
                if answer == 'Coin Booster':
                    if total_coins - 1 >= store_items['Coin Booster'][0]:
                        total_coins -= store_items['Coin Booster'][0]
                        coin_boost_active = True
                        print(f'You just bought Coin Booster!')
                        print(f'\n'         '')
                        break
                    else:
                        if total_coins - store_items[answer][0] == 0:
                            print(f'If you buy it you will have 0 coins!!!')
                            print(f'\n'      '\n'      '')
                            break
                        print(f'Not enough money!')
                        print(f'\n'      '\n'      '')
                        break

                elif answer == i and store_items[i][2] == 'Unowned':
                    # Cheking if you can buy the item
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

# Gear logic
def Gear_Func():
    # Printing all of the gear you have
    print(f'\n'      '')
    print(f'That is your gear {name}:')
    for i in body_items.keys():
        print(f'{i} => {body_items[i]}')
    print(f'\n'      '')
    print(f'Ready to continue?')
    answer = input(f'>>> ')
    print(f'\n'      '\n'      '')

# Stats Func
def Stats_Func(round, wins, looses, level, total_coins, death_cost):
    # Printing your variable
    print(f'\n'      '')
    print(f'Thoose are your stats {name}:')
    print(f'Round: {round}')
    print(f'Wins: {wins}')
    print(f'Looses: {looses}')
    print(f'Level: {level}')
    print(f'Coins: {total_coins}')
    print(f'Death charge: {death_cost}')
    print(f'')
    print(f'Ready to continue?')
    answer = input(f'>>> ')
    print(f'\n'      '')

# def LevelUp_Func():
#     level += 1
#     xp -= xp_to_lvl_up
#     xp_to_lvl_up += 20
#     print(level)
#     print(xp)
#     print(xp_to_lvl_up)
#     if level % 5 == 0:
#         print(f'\n'      '')
#         print(f'Reach Level {level}')

# Start
print(f'Welcome to "The Arcane Odyssey" player!')
print(f'Can you help our team to defeat the big monster?')
answer = input(f'>>> ')

# Making variables, lists and dictionarities
total_coins = 300
death_cost = 50
level = 1
xp = 0
xp_to_lvl_up = 10
coin_boost_active = False
round = 0
wins = 0
looses = 0

dict_helper = {'mid': 1, 'left': 2, 'right': 3}
store_items = {'Cheese Bowl': [300, 'Helmet', 'Unowned'], 'Cheese Protector': [500, 'Chest', 'Unowned', ['Saving', 10]], 'Cheese Farters': [400, 'Legs', 'Unowned'],
               'Cheese Socks': [250, 'Feet', 'Unowned'], 'Ghost Defender': [125, 'Shield', 'Unowned', {'Saving': 1}], 'Stone Cutter': [100, 'Weapon', 'Unowned'],
               'Coin Booster': [25, 'Boosts the win from the next match with 50%']}
body_items = {'Helmet': 'None', 'Chest': 'None', 'Legs': 'None', 'Feet': 'None', 'Shield': 'Default', 'Weapon': 'Default'}
backpack = {}

name = input(f'Before we start can you enter your name? ==> ')

print(f'Ok, let\'s begin!')

print('\n'      '\n'      '')


# Description
answer = input(f'Type in "Ready" if you are ==> ')
print(f'I doesn\'t matter what you say we are starting!')
print(f'\n'      '\n'      '')
print(f'The monster is strong and you need to predict where it is going to throw a rock!')
print(f'You need to type the position you think the rock will fall if you don\'t guess it correctly you are loosing {death_cost} coins!')
print(f'Every 10th round you will loose with 25 more coins.')
print(f'Just a reminder that you have {total_coins} coins.')
print(f'Good luck!')

# Calling the main game func
Main_Game_Func(total_coins, death_cost, round, level, xp, xp_to_lvl_up, coin_boost_active, wins, looses)
