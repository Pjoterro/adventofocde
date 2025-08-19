import itertools

### test cases:
test_volume = """25"""
test_input = """20
15
10
5
5"""
test_result1 = """4"""
test_result2 = """3"""

### input file path
input_path = """.\\2015\input_day17.txt""" # specific for windows

### functions ang globals
task_volume = """150"""

def is_valid_combination(combination, volume):
    comb_vol = 0
    for co in combination:
        comb_vol += co
    return comb_vol == int(volume)

def get_all_combinations(input, volume):
    containers = []
    result = []
    for line in input.splitlines():
        containers.append(int(line))
    i = 1
    while i < len(containers):
        for comb in itertools.combinations(containers, i):
            if is_valid_combination(comb, volume):
                result.append(comb)
        i += 1
    return result

def find_least_containers(all_comb):
    least = all_comb[1]
    for comb in all_comb:
        if len(comb) < len(least):
            least = comb
    # print(least)
    least_numb = len(least)
    result = []
    for comb in all_comb:
        if len(comb) == least_numb:
            result.append(comb)
    # print(result)
    return result


### main 
# mode = "TEST"
mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
    volume = task_volume
elif mode == "TEST":
    input = test_input
    volume = test_volume

all_combinations = get_all_combinations(input, volume)
result1 = len(all_combinations)
shortest_combs = find_least_containers(all_combinations)
result2 = len(shortest_combs)

if mode == "TASK":
    print("Task 1: " + str(result1))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result1) == result1) + "\n    Expected test result 1: " + str(test_result1) + "   |   Actual test result 1: " + str(result1))
    print("Test 2: " + str(int(test_result2) == result2) + "\n    Expected test result 2: " + str(test_result2) + "   |   Actual test result 2: " + str(result2))
print()