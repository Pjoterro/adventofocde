import itertools

### test cases:
test_input = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
test_teaspoons = 100
test_result1 = [44, 56]
test_result2 = 62842880

### input file path
input_path = """.\\2015\input_day15.txt""" # specific for windows
task_teaspoons = 100

### functions
def get_ingridients(input_raw):
    result = []
    for line in input_raw.splitlines():
        ingr = []
        splitt = line.split(" ")
        ingr.append(splitt[0][:-1])
        ingr.append(int(splitt[2][:-1]))
        ingr.append(int(splitt[4][:-1]))
        ingr.append(int(splitt[6][:-1]))
        ingr.append(int(splitt[8][:-1]))
        ingr.append(int(splitt[10]))
        result.append(ingr)
    return result # [name, cap, dur, flav, text, cal]

def list_sum(in_list):
    result = 0
    for el in in_list:
        result += el
    return result

def create_all_ingr_comb(teaspoons, ingr):
    amount = []
    i = 0
    for i in range(teaspoons+1):
        amount.append(i)
    result = []
    for comb in list(itertools.permutations(amount, len(ingr))):
        if list_sum(comb) == 100:
            result.append(comb)
    return result # [ingr1, ingr2] | [ingr1, ingr2, ingr3, ingr4]

def eval_recipe(recipe, ingridients):  # [name, cap, dur, flav, text, cal]
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    i = 0
    while i < len(recipe):
        capacity += recipe[i] * ingridients[i][1]
        durability += recipe[i] * ingridients[i][2]
        flavor += recipe[i] * ingridients[i][3]
        texture += recipe[i] * ingridients[i][4]
        i += 1 
    if capacity < 0:
        capacity = 0
    if durability < 0:
        durability = 0
    if flavor < 0:
        flavor = 0
    if texture < 0:
        texture = 0
    result = capacity * durability * flavor * texture
    return result

def check_possible_recipes(input_raw, teaspoons):
    ingridients = get_ingridients(input_raw)
    possible_combs = create_all_ingr_comb(teaspoons, ingridients)
    result = 0
    best_comb = []
    for comb in possible_combs:
        if result < eval_recipe(comb, ingridients):
            result = eval_recipe(comb, ingridients)
            best_comb = comb
    return result

### main 
# mode = "TEST"
mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
    teaspoons = task_teaspoons
elif mode == "TEST":
    input = test_input
    teaspoons = test_teaspoons

result = check_possible_recipes(input, teaspoons)

if mode == "TASK":
    print("Task 1: " + str(result))
    # print("Task 2: " + str(result))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result2) == result) + "\n    Expected test result 1: " + str(test_result2) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()