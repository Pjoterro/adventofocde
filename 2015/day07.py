### test cases:
test = """x AND y -> d
x OR y -> e
123 -> x
x LSHIFT 2 -> f
y RSHIFT 2 -> g
456 -> y
NOT x -> h
NOT y -> i"""
test_result = """d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456"""

### input file path
input_path = """.\\2015\input_day07.txt""" # specific for windows

### functions and globals

wire_dict = dict()
task_list = []
future_task_list = []

def translate_line(line):
    contents = line.split(" ")
    translation = []
    if "AND" in line or "OR" in line or "LSHIFT" in line or "RSHIFT" in line:
        translation.append(contents[1])
        translation.append(contents[0])
        translation.append(contents[2])
        translation.append(contents[4])
    elif "NOT" in line:
        translation.append(contents[0])
        translation.append(contents[1])
        translation.append(0)
        translation.append(contents[3])
    else:
        translation.append("PROVIDE")
        translation.append(contents[0])
        translation.append(0)
        translation.append(contents[2])
    return translation
        
#TODO: sth wrong with first if - redo
def perform_action(translation): # [action, input1, input2, output]
    if translation[0] is not "PROVIDE" and (translation[1] not in wire_dict.keys() or (translation[2] not in wire_dict.keys() and not isinstance(translation[2], int))):
        return False # operation not succesful, not enough inputs
    if translation[0] == "PROVIDE":
        wire_dict[translation[3]] = int(translation[1])
    elif translation[0] == "AND":
        wire_dict[translation[3]] = wire_dict[translation[1]] & wire_dict[translation[2]]
    elif translation[0] == "OR":
        wire_dict[translation[3]] = wire_dict[translation[1]] | wire_dict[translation[2]]
    elif translation[0] == "LSHIFT":
        wire_dict[translation[3]] = wire_dict[translation[1]] << int(translation[2])
    elif translation[0] == "RSHIFT":
        wire_dict[translation[3]] = wire_dict[translation[1]] >> int(translation[2])
    elif translation[0] == "NOT":
        wire_dict[translation[3]] = ~wire_dict[translation[1]]
    return True

### main 
# mode = "TASK"
mode = "TEST"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
    looking_for = 'a'
elif mode == "TEST":
    input = test
    looking_for = 'd'

task_list = input.splitlines()
while True:
    for task in task_list:
        if not perform_action(translate_line(task)):
            future_task_list.append(task)
    print(wire_dict)
    if len(future_task_list) > 0:
        task_list = future_task_list.copy()
        future_task_list.clear()
    else:
        break

result = wire_dict[looking_for]
print(result)

if mode == "TASK":
    print("Task 1: " + str(result))
    # print("Task 2: " + str(result))
# elif mode == "TEST":
#     print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
#     print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
# print()