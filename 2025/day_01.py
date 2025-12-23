### other consts
start_position = 50

### test cases:
test_input = """R1000
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
test_result_1 = """3"""
test_result_2 = """16"""


### input file path
input_path = """.\\2025\inputs\input_day_01.txt""" # specific for windows

### functions
def count_zero_positions(input):
    current_pos = start_position
    result = 0
    for line in input.splitlines():
        steps = int(line[1:])
        if line[0] == 'L':
            steps = -steps
        current_pos = current_pos + steps
        while current_pos < 0 or current_pos > 99:
            if current_pos < 0:
                current_pos = 100 + current_pos
            if current_pos > 99:
                current_pos = current_pos - 100
        if current_pos == 0:
            result += 1
    return result

def count_all_zeros(input):
    current_pos = start_position
    result = 0
    for line in input.splitlines():
        print("new cycle, current pos: ", current_pos, " | results: ", result)
        is_already_incremented = False
        steps = int(line[1:])
        if steps > 100:
            result += int(steps / 100)
            steps = steps % 100
            print("steps reduced; result: ", result, " | new steps: ", steps)
        if line[0] == 'L':
            steps = -steps
            print("steps switched - new steps: ", steps)
        previous_pos = current_pos
        current_pos = current_pos + steps
        print("new pos: ", current_pos)
        if current_pos < 0 or current_pos > 99:
            if current_pos < 0:
                current_pos = 100 + current_pos
                print("rollback LEFT: ", current_pos)
                if not previous_pos == 0:
                    print("prevoius pos: ", previous_pos, " | current_pos: ", current_pos)
                    result += 1
                is_already_incremented = True
            if current_pos > 99:
                current_pos = current_pos - 100
                print("rollback RIGHT: ", current_pos)
                if True:
                    print("prevoius pos: ", previous_pos, " | current_pos: ", current_pos)
                    result += 1
                    is_already_incremented = True
            print("rollback - result: ", result, " flag: ", is_already_incremented)
        if current_pos == 0 and not is_already_incremented:
            result += 1
            print("we are on zero without rollback - current pos: ", current_pos, " | result: ", result)
        print()
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

result_1 = count_zero_positions(input)
result_2 = count_all_zeros(input)

if mode == "TEST":
    print("Test 1: " + str(int(test_result_1) == result_1) + "\n    Expected test result 1: " + str(test_result_1) + "   |   Actual test result 1: " + str(result_1))
    print("Test 2: " + str(int(test_result_2) == result_2) + "\n    Expected test result 2: " + str(test_result_2) + "   |   Actual test result 2: " + str(result_2))
if mode == "TASK":
    print("Task 1: " + str(result_1))
    print("Task 2: " + str(result_2))
print()