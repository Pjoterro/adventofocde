### test cases:
test_input = """3-5
10-14
16-20
12-18
9-21

1
5
8
11
17
32"""
test_result_1 = """3"""
test_result_2 = """16"""

### input file path
input_path = """.\\2025\inputs\input_day_05.txt""" # specific for windows

### functions
def split_input(input):
    flag = True
    fresh_ids = []
    ingredients = []
    for line in input.splitlines():
        if line == '':
            flag = False
            continue
        if flag:
            pair = [int(line.split('-')[0]), int(line.split('-')[1])]
            fresh_ids.append(pair)
        else:
            ingredients.append(int(line))
    return [fresh_ids, ingredients]

def assess_ingredients(input):
    fresh_ids = split_input(input)[0]
    ingredients = split_input(input)[1]
    result = 0
    for ing in ingredients:
        for rule in fresh_ids:
            if ing >= rule[0] and ing <= rule[1]:
                result += 1
                break
    return result

def split_input_v2(input):
    fresh_ids = []
    for line in input.splitlines():
        if line == '':
            break
        pair = [int(line.split('-')[0]), int(line.split('-')[1])]
        fresh_ids.append(pair)
    return fresh_ids

def are_ids_everlapping(id1, id2):
    test1 = id1[0] >= id2[0] and id1[0] <= id2[1]
    test2 = id1[1] >= id2[0] and id1[1] <= id2[1]
    test3 = id1[0] < id2[0] and id1[1] > id2[1]
    test4 = id1[0] > id2[0] and id1[1] < id2[1]
    return test1 or test2 or test3 or test4

def merge_two_ids(id1, id2):
    min = id1[0]
    max = id1[1]
    if id2[0] < id1[0]:
        min = id2[0]
    if id2[1] > id1[1]:
        max = id2[1]
    return [min, max]

def merge_fresh_id_ranges(input):
    current_ids = split_input(input)[0]
    future_ids = []
    change_flag = True
    iterations = 0
    while change_flag:
        print(iterations)
        iterations += 1
        change_flag = False
        for i in range(0, len(current_ids)):
            overlapping_flag = False
            for j in range(len(future_ids)):
                if are_ids_everlapping(current_ids[i], future_ids[j]):
                    merged = merge_two_ids(current_ids[i], future_ids[j])
                    print("Merging: ", current_ids[i], " + ", future_ids[j], " = ", merged)
                    future_ids.append(merged)
                    future_ids.remove(future_ids[j])
                    overlapping_flag = True
                    change_flag = True
                    break                    
            if not overlapping_flag:
                future_ids.append(current_ids[i])
        current_ids.clear()
        current_ids = future_ids.copy()
        future_ids.clear()
    return current_ids

def count_all_ids_v2(input):
    result = 0
    for min_max_range in merge_fresh_id_ranges(input):
        result += (min_max_range[1] + 1) - min_max_range[0]
    return result

### main 
# mode = "TEST"
mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
elif mode == "TEST":
    input = test_input

print("Part I started...")
result_1 = assess_ingredients(input)
print("Part I ended!")
print("Part II started...")
result_2 = count_all_ids_v2(input)
print("Part II ended!")

if mode == "TEST":
    print("Test 1: " + str(int(test_result_1) == result_1) + "\n    Expected test result 1: " + str(test_result_1) + "   |   Actual test result 1: " + str(result_1))
    print("Test 2: " + str(int(test_result_2) == result_2) + "\n    Expected test result 2: " + str(test_result_2) + "   |   Actual test result 2: " + str(result_2))
elif mode == "TASK":
    print("Task 1: " + str(result_1))
    print("Task 2: " + str(result_2))
print()