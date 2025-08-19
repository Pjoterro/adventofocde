### test input
test_input = """Sue 4: perfumes: 2, vizslas: 0, cars: 6
Sue 5: goldfish: 1, trees: 3, perfumes: 10
Sue 6: children: 9, vizslas: 7, cars: 9"""

### input file path
input_path = """.\\2015\input_day16.txt""" # specific for windows

### functions and globals
correct_sue = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

def parse_aunt_candidate(line): # Sue 1: goldfish: 6, trees: 9, akitas: 0
    result = dict()
    elements = line.split(" ")
    result["Sue"] = elements[1][:-1]
    i = 2
    while i < len(elements): # = 8
        result[elements[i]] = elements[i+1].strip(",")
        i += 2
    return result

def parse_input(input):
    result = []
    for line in input.splitlines():
        result.append(parse_aunt_candidate(line))
    return result

def is_correct_sue(candidate):
    correct_aunt = dict()
    elements = correct_sue.splitlines()
    for ele in elements:
        correct_aunt[ele.split(" ")[0]] = ele.split(" ")[1]
    for key in candidate.keys():
        if key == "Sue":
            continue
        if candidate[key] != correct_aunt[key]:
            return False
    print(candidate["Sue"])
    return True

### main 
# mode = "TEST"
mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
elif mode == "TEST":
    input = test_input

for aunt in parse_input(input):
    if is_correct_sue(aunt):
        print(aunt)

if mode == "TASK":
    print()
    # print("Task 1: " + str(result))
    # print("Task 2: " + str(result))
elif mode == "TEST":
    print()
    # print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()