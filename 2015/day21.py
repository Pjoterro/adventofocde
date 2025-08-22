import itertools

### test cases:
test = """"""
test_result = """"""

### input file path
input_path = """.\\2015\input_day21.txt""" # specific for windows

### functions
player = [100, 0, 0] # hp, armor, damage
boss = [109, 2, 8] # hp, armor, damage

weapons = [["Dagger", 8, 4, 0], ["Shortsword", 10, 5, 0], ["Warhammer", 25, 6, 0], ["Longsword", 40, 7, 0], ["Greataxe", 74, 8, 0]]
armors = [["None", 0, 0, 0], ["Leather", 13, 0, 1], ["Chainmail", 31, 0, 2], ["Splintmail", 53, 0, 3], ["Bandedmail", 75, 0, 4], ["Platemail", 102, 0, 5]]
rings = [["None", 0, 0, 0], ["None", 0, 0, 0], ["Damage +1", 25, 1, 0], ["Damage +2", 50, 2, 0], ["Damage +3", 100, 3, 0], ["Defense +1", 20, 0, 1], ["Defense +2", 40, 0, 2], ["Defense +3", 80, 0, 3]]

def generate_all_items_combo():
    global weapons, armors, rings
    rings_comb = list(itertools.combinations(rings, 2))
    weapon_comb = weapons
    armor_comb = armors
    result = []
    for weap in weapon_comb:
        for arm in armor_comb:
            for rin in rings_comb:
                result.append([weap, arm, rin[0], rin[1]])
    return result

def calculate_gear(gear_comb):
    armor_bonus = 0
    damage_bonus = 0
    gear_cost = 0
    for item in gear_comb:
        gear_cost += item[1]
        damage_bonus += item[2]
        armor_bonus += item[3]
    return [gear_cost, armor_bonus, damage_bonus]

def is_player_winning_fight(boss, player, gear_bonus):
    boss_buffor = list(boss)
    player_buffor = list(player)
    while True:
        dmg_to_boss = player[2] + gear_bonus[2] - boss[1]
        if dmg_to_boss < 1:
            dmg_to_boss = 1
        boss_buffor[0] -= dmg_to_boss
        if boss_buffor[0] <= 0:
            return True
        dmg_to_player = boss[2] - (player[1] + gear_bonus[1])
        if dmg_to_player < 1:
            dmg_to_player = 1
        player_buffor[0] -= dmg_to_player
        if player_buffor[0] <= 0:
            return False
        
def find_cheapes_winning_gear():
    global player, boss
    result = []
    for gear_set in generate_all_items_combo():
        if is_player_winning_fight(boss, player, calculate_gear(gear_set)):
            result.append(gear_set)
    cheapest_gear = result[0]
    price = calculate_gear(cheapest_gear)[0]
    for gear in result:
        if calculate_gear(gear)[0] < price:
            cheapest_gear = gear
            price = calculate_gear(gear)[0]
    return cheapest_gear

def find_priciest_loosing_gear():
    global player, boss
    result = []
    for gear_set in generate_all_items_combo():
        if not is_player_winning_fight(boss, player, calculate_gear(gear_set)):
            result.append(gear_set)
    priciest_gear = result[0]
    price = calculate_gear(priciest_gear)[0]
    for gear in result:
        if calculate_gear(gear)[0] > price:
            priciest_gear = gear
            price = calculate_gear(gear)[0]
    return priciest_gear

### main 
# mode = "TEST"
mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
elif mode == "TEST":
    input = test

cheapest_gear = find_cheapes_winning_gear()
print(cheapest_gear)
result = calculate_gear(cheapest_gear)[0]

priciest_gear = find_priciest_loosing_gear()
print(priciest_gear)
result2 = calculate_gear(priciest_gear)[0]

if mode == "TASK":
    print("Task 1: " + str(result))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    print()
    # print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()
