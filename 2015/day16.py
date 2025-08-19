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
        result[elements[i]] = int(elements[i+1].strip(","))
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
        correct_aunt[ele.split(" ")[0]] = int(ele.split(" ")[1])
    for key in candidate.keys():
        if key == "Sue":
            continue
        if candidate[key] != correct_aunt[key]:
            return False
    return True

def is_correct_sue_v2(candidate):
    correct_aunt = dict()
    elements = correct_sue.splitlines()
    for ele in elements:
        correct_aunt[ele.split(" ")[0]] = int(ele.split(" ")[1])
    for key in candidate.keys():
        if key == "Sue":
            continue
        elif key == "cats:" or key == "trees:":
            if candidate[key] <= correct_aunt[key]:
                return False
        elif key == "pomeranians:" or key == "goldfish:":
            if candidate[key] >= correct_aunt[key]:
                return False
        elif candidate[key] != correct_aunt[key]:
            return False
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
        result1 = aunt["Sue"]
    if is_correct_sue_v2(aunt):
        result2 = aunt["Sue"]    

if mode == "TASK":
    print()
    print("Task 1: " + str(result1))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    print()
print()