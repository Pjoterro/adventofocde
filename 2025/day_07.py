### test cases:
test_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
test_result_1 = """21"""
test_result_2 = """40"""

### input file path
input_path = """.\\2025\inputs\input_day_07.txt""" # specific for windows

### functions
def count_splits(input):
    result = 0
    input_by_line = input.splitlines()
    current_split = []
    for x in range(len(input_by_line[0])):
        if input_by_line[0][x] == '.':
            current_split.append(0)
        if input_by_line[0][x] == 'S':
            current_split.append(1)
    future_split = current_split.copy()
    for y in range(len(input_by_line)):
        for x in range(len(input_by_line[y])):
            if input_by_line[y][x] == '^' and current_split[x] == 1:
                future_split[x-1] = 1
                future_split[x] = 0
                future_split[x+1] = 1
                result += 1
            elif current_split[x] == 1:
                future_split[x] = 1
        current_split = future_split.copy()
    return result

def traverse_all_possibillities(input):
    input_by_line = input.splitlines()
    current_line = []
    for sign in input_by_line[0]:
        if sign == 'S':
            current_line.append(1)
        else:
            current_line.append(0)
    print(current_line)
    x = 2
    while x < len(input_by_line):
        future_line = current_line.copy()
        # for i in range(len(current_line)):
        #     future_line.append(0)
        for i in range(len(input_by_line[x])):
            if input_by_line[x][i] == '^':
                future_line[i-1] += current_line[i]
                future_line[i+1] += current_line[i]
        for i in range(len(input_by_line[x])):
            if input_by_line[x][i] == '^':
                future_line[i] = 0
        current_line = future_line.copy()
        x += 2
    print(current_line)
    result = 0
    for numb in current_line:
        result += numb
    return result

    
    

def traverse_every_path(pos, board):
    if len(board) > 2:
        if board[0][pos] == '^':
            return traverse_every_path(pos-1, board[2:]) + traverse_every_path(pos+1, board[2:])
        else:
            return traverse_every_path(pos, board[2:])
    elif len(board) == 2:
        if board[0][pos] == '^':
            return 2
        else:
            return 1
    else:
        print("ERROR")
        
def count_all_timelines(input):
    input_by_line = input.splitlines()
    x = 0
    for x in range(len(input_by_line[0])):
        if input_by_line[0][x] == 'S':
            break
    result = traverse_every_path(x, input_by_line[2:])
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
result_1 = count_splits(input)
print("Part I ended!")
print("Part II started...")
result_2 = traverse_all_possibillities(input)
print("Part II ended!")

if mode == "TEST":
    print("Test 1: " + str(int(test_result_1) == result_1) + "\n    Expected test result 1: " + str(test_result_1) + "   |   Actual test result 1: " + str(result_1))
    print("Test 2: " + str(int(test_result_2) == result_2) + "\n    Expected test result 2: " + str(test_result_2) + "   |   Actual test result 2: " + str(result_2))
elif mode == "TASK":
    print("Task 1: " + str(result_1))
    print("Task 2: " + str(result_2))
print()