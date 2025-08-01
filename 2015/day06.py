### test cases:
test_map_size = 5
test_instruction = """turn on 1,1 through 4,4
toggle 0,2 through 4,3
turn off 2,0 through 2,4
turn off 2,3 through 3,4
toggle 0,0 through 3,1
turn on 1,0 through 1,4
toggle 4,4 through 4,4"""
test_result = """13"""

task_map_size = 1000

### input file path
input_path = """.\\2015\input_day06.txt""" # specific for windows

### functions
def create_map(size):
    map = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(-1)
        map.append(line)
    return map

def create_new_map(size):
    map = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(0)
        map.append(line)
    return map

def translate_line(line):
    translation = []
    elements = line.split(" ")
    if "turn" in elements:
        elements.remove("turn")
    translation.append(elements[0]) # action
    translation.append(int(elements[1].split(",")[0])) # X start
    translation.append(int(elements[1].split(",")[1])) # Y start
    translation.append(int(elements[3].split(",")[0])) # X stop
    translation.append(int(elements[3].split(",")[1])) # Y stop
    return translation # [action, Xstart, Ystart, Xstop, Ystop]

def apply_changes(lamp_map, translation):
    for i in range(translation[1], translation[3] + 1):
        for j in range(translation[2], translation[4] + 1):
            if translation[0] == "on":
                lamp_map[i][j] = 1
            elif translation[0] == "off":
                lamp_map[i][j] = -1
            elif translation[0] == "toggle":
                lamp_map[i][j] *= -1
            else:
                print("wrong translation")
                return False
    return True

def apply_proper_change(lamp_map, translation):
    for i in range(translation[1], translation[3] + 1):
        for j in range(translation[2], translation[4] + 1):
            if translation[0] == "on":
                lamp_map[i][j] += 1
            elif translation[0] == "off":
                lamp_map[i][j] -= 1
                if lamp_map[i][j] < 0:
                    lamp_map[i][j] = 0
            elif translation[0] == "toggle":
                lamp_map[i][j] += 2
            else:
                print("wrong translation")
                return False
    return True

def get_lit_lamps(lamp_map):
    result = 0
    for line in lamp_map:
        for lamp in line:
            if lamp == 1:
                result += 1
    return result

def get_total_brightness(lamp_map):
    result = 0
    for line in lamp_map:
        for lamp in line:
            result += lamp
    return result

def print_map(lamp_map):
    for line in lamp_map:
        print_line = ""
        for lamp in line:
            if lamp == 1:
                print_line = print_line + " " + str(lamp) + " "
            else:
                print_line = print_line + str(lamp) + " "
        print(print_line)
    
### main 
mode = "TASK"
# mode = "TEST"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
    map_size = task_map_size
    instruction = input
elif mode == "TEST":
    map_size = test_map_size
    instruction = test_instruction
    result = test_result
    
lamp_map = create_map(map_size)
for line in instruction.splitlines():
    apply_changes(lamp_map, translate_line(line))
result1 = get_lit_lamps(lamp_map)

new_lamp_map = create_new_map(map_size)
for line in instruction.splitlines():
    apply_proper_change(new_lamp_map, translate_line(line))
result2 = get_total_brightness(new_lamp_map)

if mode == "TASK":
    print("Task 1: " + str(result1))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()