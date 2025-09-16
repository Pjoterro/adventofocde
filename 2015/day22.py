import itertools

### test cases:
test = """"""
test_result = """"""

### input file path
test_player_hp = 10
test_player_mana = 250
test_boss_hp_1 = 13
test_boss_hp_2 = 14
test_boss_dmg = 8

test_result_1 = 226 # Poison (173) - Magic Missle (53)
test_result_2 = 641 # Recharge (229) - Shield (113) - Drain (73) - Poison (173) - Magic Missle (53)

task_player_hp = 50
task_player_mana = 500
task_boss_hp = 55
task_boss_dmg = 8

### spells
# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

# [name, mana usage, turns] if turns = -1 it is instant spell, if it is > 0 it is action over time
spells = [["MM", 53, -1], ["D", 73, -1], ["SH", 113, 6], ["P", 173, 6], ["R", 229, 5]]

### functions
def is_combination_correct(combination): # checking if spells over time are not cast too often
    last_index = -1
    for spell in ["SH", "P", "R"]:
        last_index = -1
        i = 0
        turn = 1
        while i < len(combination):
            if last_index == -1 and combination[i] == spell: # finding first index
                last_index = turn
            if combination[i] == spell and last_index >= 0 and turn-last_index < 6:
                return False
            i += 1
            turn += 2
    return True

def generate_correct_combs(player_hp):
    spell_list = ["MM", "D", "SH", "P", "R"]
    all_comb = itertools.product(spell_list, repeat=player_hp)
    result = []
    for combination in all_comb:
        if is_combination_correct(combination):
            result.append(combination)
    print(len(result), " correct spells combinations")
    return result

def single_game(game_input): # game_input = [player_hp, player_mana, boss_hp, boss_dmg, spell_order]
    player_hp = game_input[0]
    player_mana = game_input[1]
    player_armor = 0
    boss_hp = game_input[2]
    boss_dmg = game_input[3]
    active_spells = []
    spell_order = game_input[4]
    while True:
        # Tura gracza
        # Wykonaj zalegle zaklecia w kolejce
        for spell in active_spells:
            pass
        # rzuc nowe zaklecie
        # wykonaj jesli to zaklecie natychmiastowe
        # dodaj do kolejki i wykonaj pozniej jesli to zaklecie over time

        # Tura bossa
        # wykonaj zaklecia i efekty w kolejce
            

    return mana_usage # -1 = player was killed/run out of mana or boss was NOT killed

### main 
mode = "TEST"
# mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    player_hp = task_player_hp
    player_mana = task_player_mana
    boss_hp = task_boss_hp
    boss_dmg = task_boss_dmg

elif mode == "TEST":
    player_hp = test_player_hp
    player_mana = test_player_mana
    boss_hp = test_boss_hp_1
    boss_dmg = test_boss_dmg

result = TEMPLATE(input)

if mode == "TASK":
    print("Task 1: " + str(result))
    # print("Task 2: " + str(result))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()
