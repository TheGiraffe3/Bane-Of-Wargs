import yaml
import random
import os
import sys
import time
import enquiries
from colors import *
from colorama import Fore, Back, Style, init, deinit

# initialize colorama
init()

# battle stats
defend = 0
turn = True
fighting = True

def print_long_string(text):
    new_input = ""
    for i, letter in enumerate(text):
        if i % 54 == 0:
            new_input += '\n'
        new_input += letter

    # this is just because at the beginning too a `\n` character gets added
    new_input = new_input[1:]
    print(str(new_input))

def print_separator(character):
    count = 0

    while count < 55:
        sys.stdout.write(COLOR_STYLE_BRIGHT + character + COLOR_RESET_ALL)
        sys.stdout.flush()
        count += 1
    sys.stdout.write('\n')

def calculate_player_risk(player, item, enemies_remaining, choosen_enemy, enemy):
    # get all stats
    player_hp = player["health"]
    player_agi = player["agility"]
    player_prot = player["armor protection"]
    player_av_dmg = ( item[player["held item"]]["damage"] + 1 ) / 2
    player_def = item[player["held item"]]["defend"]
    player_critic_ch = item[player["held item"]]["critical hit chance"]
    player_health_cap = 1 # placeholder
    enemies_number = enemies_remaining
    enemy_health = random.randint(choosen_enemy["health"]["min spawning health"], choosen_enemy["health"]["max spawning health"])
    enemy_agility = choosen_enemy["agility"]
    enemy_max_damage = choosen_enemy["damage"]["max damage"]
    enemy_min_damage = choosen_enemy["damage"]["min damage"]
    enemy_critical_chance = choosen_enemy["damage"]["critical chance"]

    # calculate player health capabilities (how many HP the player can restore)
    count = 0
    player_inventory = player["inventory"]
    player_inventory_len = len(player_inventory) - 1
    current_item_health_restoration = 0
    item_health_bonus = 0
    while count < player_inventory_len:

        selected_item = player_inventory[count]

        if item[selected_item]["type"] == "Food" or item[selected_item]["type"] == "Consumable":
            item_health_restoration = item[selected_item]["healing level"]
            item_health_bonus = item[selected_item]["max bonus"]
            if item_health_restoration == "max level":
                current_item_health_restoration = player["max health"]
            else:
                current_item_health_restoration = int(item_health_restoration)
            if item_health_bonus != 0:
                item_health_bonus = int(item[selected_item]["max bonus"]) / 2


        player_health_cap += current_item_health_restoration
        player_health_cap += item_health_bonus

        count += 1

    # get differences between player and enemy
    hp_diff = player_hp - enemy_health
    agi_diff = player_agi - enemy_agility
    av_dmg_diff = player_av_dmg - ( ( enemy_max_damage + enemy_min_damage ) / 2 )
    critic_ch_diff = player_critic_ch - enemy_critical_chance

    # compute percentage of defeat chance
    defeat_percentage = ( ( ( ( hp_diff / 1.4) - ( agi_diff / 1.2 ) - ( player_prot / 1.1 ) - ( av_dmg_diff / 1.3 ) + ( player_def / 1.4 ) - ( critic_ch_diff / 0.1 ) ) * ( player_health_cap / 15.24 ) ) * ( enemies_number / 1.5 ) )
    defeat_percentage = round(defeat_percentage, 0)
    defeat_percentage = int(defeat_percentage)

    return defeat_percentage

def encounter_text_show(player, item, enemy, map, map_location, enemies_remaining, lists, defeat_percentage):
    # import stats
    global turn, defend, fighting, already_encountered
    global enemy_singular, enemy_plural, enemy_max, enemy_health, enemy_max_damage, enemy_min_damage, enemy_agility, enemy_damage, choosen_item
    player_agility = player["agility"]
    print(" ") # do not merge with possible actions text
    # load and create enemies list type

    health_color = COLOR_GREEN
    enemies_number = enemies_remaining

    text = '='
    print_separator(text)

    if enemies_number > 1:
        print("You encounter a group of " + str(enemy_plural) + " that won't let you pass.")
    else:
        print("You find a/an " + str(enemy_singular) + " on your way.")

    # player stats updates
    risk = defeat_percentage

    # display
    bars = 10
    remaining_risk_symbol = "█"
    lost_risk_symbol = "_"

    remaining_risk_bars = round(risk / 100 * bars)
    lost_risk_bars = bars - remaining_risk_bars

    # print HP stats and possible actions for the player

    if risk > 0.80 * 100:
        health_color = COLOR_STYLE_BRIGHT + COLOR_RED
    elif risk > 0.60 * 100:
        health_color = COLOR_RED
    elif risk > 0.45 * 100:
        health_color = COLOR_YELLOW
    elif risk > 0.30 * 100:
        health_color = COLOR_GREEN
    else:
        health_color = COLOR_STYLE_BRIGHT + COLOR_GREEN

    sys.stdout.write(f"RISK: {risk} / 100\n")
    sys.stdout.write(f"|{health_color}{remaining_risk_bars * remaining_risk_symbol}{lost_risk_bars * lost_risk_symbol}{COLOR_RESET_ALL}|\n")
    sys.stdout.flush()

    print("[R]un Away, [F]ight, [U]se Item? ")

    text = '='
    print_separator(text)

    print(" ")
    startup_action = input("> ")
    print("")

    text = '='
    print_separator(text)

    if startup_action.lower().startswith('r'):
        # run away chance
        if player["agility"] / round(random.uniform(1.10, 1.25), 2) > enemy_agility:
            print("You succeeded in running away from your enemy!")
            fighting = False
        else:
            text = "You failed in running away from your enemy! You now have to fight him/them!"
            print_long_string(text)
            text = '='
            print_separator(text)
            fighting = True
    elif startup_action.lower().startswith('f'):
            pass
    elif startup_action.lower().startswith('u'):
        player_inventory = str(player["inventory"])
        player_inventory = player_inventory.replace("'", '')
        player_inventory = player_inventory.replace("[", ' -')
        player_inventory = player_inventory.replace("]", '')
        player_inventory = player_inventory.replace(", ", '\n -')
        print("INVENTORY:")
        print(player_inventory)
        item_input = input("> ")
        # use item
        if item_input in player["inventory"]:
            if item[item_input]["type"] == "Consumable" or item[item_input]["type"] == "Food":
                if item[item_input]["healing level"] == "max health":
                    player["health"] = player["max health"]
                else:
                    player["health"] += item[item_input]["healing level"]
                player["max health"] += item[item_input]["max bonus"]
                player["inventory"].remove(item_input)
            # hold weapon/armor piece if it is one
            if item_input in player["inventory"] and item[item_input]["type"] == "Weapon":
                player["held item"] = item_input
                print("You are now holding a/an ", player["held item"])
            elif item_input in player["inventory"] and item[item_input]["type"] == "Armor Piece: Chestplate":
                player["held chestplate"] = item_input
                print("You are now wearing a/an ", player["held chestplate"])
            elif item_input in player["inventory"] and item[item_input]["type"] == "Armor Piece: Leggings":
                player["held leggings"] = item_input
                print("You are now wearing a/an ", player["held leggings"])
            elif item_input in player["inventory"] and item[item_input]["type"] == "Armor Piece: Boots":
                player["held boots"] = item_input
                print("You are now wearing a/an ", player["held boots"])
            elif item_input in player["inventory"] and item[item_input]["type"] == "Armor Piece: Sheild":
                player["held shield"] = item_input
                print("You are now holding a/an ", player["held shield"])
            text = '='
            print_separator(text)
    else:
        print("'" + startup_action + "' is not a valid option")


    print(" ")

def get_enemy_stats(player, item, enemy, map, map_location, lists, choose_rand_enemy, choosen_enemy, choosen_item, enemy_items_number, enemy_total_inventory, enemies_remaining):
    global enemy_singular, enemy_plural, enemy_max, enemy_health, enemy_max_damage, enemy_min_damage, enemy_agility, enemy_damage
    # load enemy stat

    # enemy stats
    enemy_singular = choose_rand_enemy
    enemy_plural = choosen_enemy["plural"]
    enemy_max = choosen_enemy["health"]["max health level"]
    enemy_health = random.randint(choosen_enemy["health"]["min spawning health"], choosen_enemy["health"]["max spawning health"])
    enemy_max_damage = choosen_enemy["damage"]["max damage"]
    enemy_min_damage = choosen_enemy["damage"]["min damage"]
    enemy_critical_chance = choosen_enemy["damage"]["critical chance"]
    enemy_damage = 0
    enemy_agility = choosen_enemy["agility"]

    if choose_rand_enemy not in player["enemies list"]:
        player["enemies list"].append(choose_rand_enemy)

def fight(player, item, enemy, map, map_location, enemies_remaining, lists):
    # import stats
    global turn, defend, fighting, already_encountered
    global enemy_singular, enemy_plural, enemy_max, enemy_health, enemy_max_damage, enemy_min_damage, enemy_agility, enemy_damage, choosen_item
    armor_protection = player["armor protection"]
    player_agility = player["agility"]
    # load and create enemies list type

    enemies_number = map["point" + str(map_location)]["enemy"]

    enemy_max_health = enemy_health

    critical_hit_chance = item[player["held item"]]["critical hit chance"]

    # while the player is still fighting (for run away)

    while fighting:
        # while player still alive
        # colors
        color_green = "\033[92m"
        color_yellow = "\33[33m"
        color_red = "\033[91m"
        color_blue = "\33[34m"
        color_default = "\033[0m"
        health_color = color_green
        health_color_enemy = color_blue

        while player["health"] > 0:
            while turn:
                # player stats updates
                player_health = player["health"]
                player_max_health = player["max health"]

                # display
                bars = 20
                remaining_health_symbol = "█"
                lost_health_symbol = "_"

                remaining_health_bars = round(player_health / player_max_health * bars)
                lost_health_bars = bars - remaining_health_bars

                remaining_health_bars_enemy = round(enemy_health / enemy_max_health * bars)
                lost_health_bars_enemy = bars - remaining_health_bars_enemy

                # print HP stats and possible actions for the player

                if player_health > 0.66 * player_max_health:
                    health_color = color_green
                elif player_health > 0.33 * player_max_health:
                    health_color = color_yellow
                else:
                    health_color = color_red

                if enemy_health > 0.66 * enemy_max_health:
                    health_color_enemy = color_blue
                elif enemy_health > 0.33 * enemy_max_health:
                    health_color_enemy = COLOR_CYAN
                else:
                    health_color_enemy = COLOR_MAGENTA

                sys.stdout.write(f"PLAYER: {player_health} / {player_max_health}\n")
                sys.stdout.write(f"|{health_color}{remaining_health_bars * remaining_health_symbol}{lost_health_bars * lost_health_symbol}{color_default}|\n")
                sys.stdout.write(f"ENEMY: {enemy_health} / {enemy_max_health}\n")
                sys.stdout.write(f"|{health_color_enemy}{remaining_health_bars_enemy * remaining_health_symbol}{lost_health_bars_enemy * lost_health_symbol}{color_default}|")
                sys.stdout.flush()

                action = input("\n[A]ttack, [D]efend, [U]se Item? ")

                # if player attack
                if action.lower().startswith('a'):
                    print(" ")
                    # attack formula
                    enemy_dodged = False
                    player_critical_hit = False
                    enemy_dodge_chance = round(random.uniform(0.10, enemy_agility), 2)
                    critical_hit_chance_formula = round(critical_hit_chance / random.uniform(0.03, critical_hit_chance * 2.8), 2)
                    if enemy_dodge_chance > round(random.uniform(.50, .90), 2):
                        enemy_dodged = True
                        print("Your enemy dodged your attack!")
                    if critical_hit_chance / random.uniform(.20, .35) < critical_hit_chance_formula:
                        player_critical_hit = True
                        print("You dealt a critical hit to your opponent!")
                    if not enemy_dodged:
                        player_damage = random.randint(1, int(item[player["held item"]]["damage"]))
                        if player_critical_hit:
                            player_damage = player_damage * 2
                        enemy_health -= player_damage
                        print("You dealt " + str(player_damage) + " damage to your enemy.")
                    turn = False

                # if player defend
                elif action.lower().startswith('d'):
                    print(" ")
                    defend += random.randint(0, int(item[player["held item"]]["defend"])) * player_agility
                    # defend formula
                    player["health"] += random.randint(0, 3)
                    if player["health"] > player["max health"]:
                        player["health"] = player["max health"]
                    turn = False

                # if player use an item
                elif action.lower().startswith('u'):
                    player_inventory = str(player["inventory"])
                    player_inventory = player_inventory.replace("'", '')
                    player_inventory = player_inventory.replace("[", ' -')
                    player_inventory = player_inventory.replace("]", '')
                    player_inventory = player_inventory.replace(", ", '\n -')
                    print(" ")
                    text = '='
                    print_separator(text)
                    print("INVENTORY:")
                    print(player_inventory)
                    item_input = input("> ")
                    # use item
                    if item_input in player["inventory"]:
                        if item[item_input]["type"] == "Consumable" or item[item_input]["type"] == "Food":
                            if item[item_input]["healing level"] == "max health":
                                player["health"] = player["max health"]
                            else:
                                player["health"] += item[item_input]["healing level"]
                            player["max health"] += item[item_input]["max bonus"]
                            player["inventory"].remove(item_input)
                        # hold weapon/armor piece if it is one
                        if item_input in player["inventory"] and item[item_input]["type"] == "Weapon":
                            player["held item"] = item_input
                            print("You are now holding a/an ", player["held item"])
                        elif item_input in player["inventory"] and item[item_input]["type"] == "Armor Piece: Chestplate":
                            player["held chestplate"] = item_input
                            print("You are now wearing a/an ", player["held chestplate"])
                        elif item_input in player["inventory"] and item[item_input]["type"] == "Armor Piece: Leggings":
                            player["held leggings"] = item_input
                            print("You are now wearing a/an ", player["held leggings"])
                        elif item_input in player["inventory"] and item[item_input]["type"] == "Armor Piece: Boots":
                            player["held boots"] = item_input
                            print("You are now wearing a/an ", player["held boots"])
                        elif item_input in player["inventory"] and item[item_input]["type"] == "Armor Piece: Sheild":
                            player["held shield"] = item_input
                            print("You are now holding a/an ", player["held shield"])
                        text = '='
                        print_separator(text)
                        print(" ")
                else:
                    print("'" + action + "' is not a valid option")
                    print(" ")
            # when it's not player turn
            while not turn:
                # if enemy is still alive
                if enemy_health > 0:
                    damage = random.randint(enemy_min_damage, enemy_max_damage) - defend * ( armor_protection * round(random.uniform(0.50, 0.90), 1) )
                    damage = round(damage)
                    defend = 0
                    player_dodged = False
                    enemy_critical_hit = False
                    player_dodge_chance = round(random.uniform(0.10, player_agility), 2)
                    critical_hit_chance_formula = round(critical_hit_chance / random.uniform(0.03, critical_hit_chance * 2.8), 2)
                    if critical_hit_chance / random.uniform(.20, .35) < critical_hit_chance_formula:
                        enemy_critical_hit = True
                        print("Your enemy dealt a critical hit!")
                    elif player_dodge_chance > round(random.uniform(.50, .90), 2):
                        player_dodged = True
                        print("You dodged your enemy attack!")
                    if damage > 0 and not player_dodged:
                        if enemy_critical_hit:
                            damage = damage * 2
                        player["health"] -= damage
                        print("The enemy dealt ", str(damage), " points of damage.")
                    print(" ")
                    turn = True
                else:
                    print(" ")
                    # check if any health is negative
                    if player["health"] < 0:
                        player["health"] = 0
                    if enemy_health < 0:
                        enemy_health = 0
                    remaining_health_bars = round(player_health / player_max_health * bars)
                    lost_health_bars = bars - remaining_health_bars

                    remaining_health_bars_enemy = round(enemy_health / enemy_max_health * bars)
                    lost_health_bars_enemy = bars - remaining_health_bars_enemy
                    sys.stdout.write(f"PLAYER: {player_health} / {player_max_health}\n")
                    sys.stdout.write(f"|{health_color}{remaining_health_bars * remaining_health_symbol}{lost_health_bars * lost_health_symbol}{color_default}|\n")
                    sys.stdout.write(f"ENEMY: {enemy_health} / {enemy_max_health}\n")
                    sys.stdout.write(f"|{health_color_enemy}{remaining_health_bars_enemy * remaining_health_symbol}{lost_health_bars_enemy * lost_health_symbol}{color_default}|")
                    sys.stdout.flush()
                    print("\n")
                    player["xp"] += enemy_max * enemy_max_damage / 3
                    player["health"] += random.randint(0, 3)
                    enemies_remaining -= 1
                    still_playing = False
                    return
        return



still_playing = True

# deinitialize colorama
deinit()
