### test cases:
test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
test_result_1 = """13"""
test_result_2 = """43"""

### input file path
input_path = """.\\2025\inputs\input_day_04.txt""" # specific for windows

### functions
def count_accessible(input):
    input_map = input.splitlines()
    result = 0
    for y in range(len(input_map)):
        for x in range(len(input_map[0])):
            if input_map[y][x] == '@':
                neighbours = [[x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y], [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]]
                count = 0
                for pair in neighbours:
                    if pair[0] < 0 or pair[0] >= len(input_map[0]) or pair[1] < 0 or pair[1] >= len(input_map):
                        continue
                    if input_map[pair[1]][pair[0]] == '@':
                        count += 1
                if count < 4:
                    result += 1
    return result

def count_all_possible(input):
    current_map = input.splitlines()
    next_map = []
    result = 0
    flag = True
    while flag:
        flag = False
        next_map.clear()
        for y in range(len(current_map)):
            next_line = ''
            for x in range(len(current_map[0])):
                if current_map[y][x] == '@':
                    neighbours = [[x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y], [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]]
                    count = 0
                    for pair in neighbours:
                        if pair[0] < 0 or pair[0] >= len(current_map[0]) or pair[1] < 0 or pair[1] >= len(current_map):
                            continue
                        if current_map[pair[1]][pair[0]] == '@':
                            count += 1
                    if count < 4:
                        result += 1
                        next_line += '.'
                        flag = True
                    else:
                        next_line += '@'
                else:
                    next_line += '.'
            next_map.append(next_line)
        current_map.clear()
        current_map = next_map.copy()
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
result_1 = count_accessible(input)
print("Part I ended!")
print("Part II started...")
result_2 = count_all_possible(input)
print("Part II ended!")

if mode == "TEST":
    print("Test 1: " + str(int(test_result_1) == result_1) + "\n    Expected test result 1: " + str(test_result_1) + "   |   Actual test result 1: " + str(result_1))
    print("Test 2: " + str(int(test_result_2) == result_2) + "\n    Expected test result 2: " + str(test_result_2) + "   |   Actual test result 2: " + str(result_2))
elif mode == "TASK":
    print("Task 1: " + str(result_1))
    print("Task 2: " + str(result_2))
print()