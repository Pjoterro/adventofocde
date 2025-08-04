### test cases:
test_result = """12"""

### input file path
test_input_path = """.\\2015\\test_input_day08.txt"""
input_path = """.\\2015\\input_day08.txt""" # specific for windows

### functions

def count_line(old_line):
    line = old_line
    in_memory = 0
    i = 0
    while i < len(line):
        in_memory += 1
        if line[i] == '\\':
            if line[i+1] == 'x':
                i += 3
            else:
                i += 1
        i += 1
    in_memory -= 2
    print(line + " | all_char: " + str(len(line)) + " | in_memory: " + str(in_memory))
    return len(line), in_memory

def count_difference(input):
    all_chars = 0
    all_in_memory = 0
    for line in input.splitlines():
        results = count_line(line)
        all_chars += results[0]
        all_in_memory += results[1]
    return all_chars - all_in_memory

### main 
mode = "TEST"
# mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
elif mode == "TEST":
    file = open(test_input_path)
    input = file.read()

result = count_difference(input)

if mode == "TASK":
    print("Task 1: " + str(result))
    # print("Task 2: " + str(result))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()