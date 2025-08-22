### test cases:
test_input = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO"""
test_result = """7"""
test_result_2 = """6"""

### input file path
input_path = """.\\2015\input_day19.txt""" # specific for windows

### functions
def create_substitute_list(input):
    result = []
    for line in input.splitlines():
        if "=>" in line:
            result.append(line.split(" => "))
    return result

def get_chemical(input):
    return input.splitlines()[-1]

def get_all_different_combinations(input):
    result = set()
    i = 0
    compound = get_chemical(input)
    subs = create_substitute_list(input)
    while i < len(compound):
        single_letter = compound[i]
        for sub in subs:
            if single_letter == sub[0]:
                buffer = compound[0:i] + sub[1] + compound[i+1:]
                result.add(buffer)
        if i < (len(compound) - 1):
            two_letters = compound[i] + compound[i+1]
            for sub in subs:
                if two_letters == sub[0]:
                    buffer = compound[0:i] + sub[1] + compound[i+2:]
                    result.add(buffer)
        i += 1
    return result

def get_longest_sub(list_of_subs):
    result = len(list_of_subs[0][1])
    for sub in list_of_subs:
        if len(sub[1]) > result:
            result = len(sub[1])
    return result

def reverse_engineer_drug(input):
    result = 0
    compound = get_chemical(input)
    subs = create_substitute_list(input)
    longest_sub = get_longest_sub(subs)
    compound_reduced = compound
    while compound_reduced != "e" and longest_sub > 0:
        reduced_flag = False
        for sub in subs:
            while len(sub[1]) == longest_sub and sub[1] in compound_reduced:
                compound_reduced = compound_reduced.replace(sub[1], sub[0], 1) # replace(x, y, 1) - bez tej jedynki zamienialo mi wszystko na raz
                reduced_flag = True
                longest_sub = get_longest_sub(subs)
                result += 1
        if not reduced_flag:
            longest_sub -= 1
    print(compound)
    print(compound_reduced)
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

drug = get_all_different_combinations(input)
result = len(drug)
result2 = reverse_engineer_drug(input)

if mode == "TASK":
    print("Task 1: " + str(result))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    print("Test 2: " + str(int(test_result_2) == result2) + "\n    Expected test result 2: " + str(test_result_2) + "   |   Actual test result 2: " + str(result2))
print()
