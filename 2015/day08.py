### test cases:
test_result = """12"""
test_result2 = """19"""

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
    # print(line + " | all_char: " + str(len(line)) + " | in_memory: " + str(in_memory))
    return len(line), in_memory

def escape_and_count(line):
    old_len = len(line)
    new_line = '\"'
    i = 0
    while i < len(line):
        if line[i] == '"':
            new_line += '\\\"'
        elif line[i] == '\\':
            new_line += '\\\\'
        else:
            new_line += line[i]
        i += 1
    new_line += '\"'
    new_len = len(new_line)
    return old_len, new_len

def count_new_len(input):
    old_lens = 0
    new_lens = 0
    for line in input.splitlines():
        buffor = escape_and_count(line)
        old_lens += buffor[0]
        new_lens += buffor[1]
    return new_lens - old_lens


def count_difference(input):
    all_chars = 0
    all_in_memory = 0
    for line in input.splitlines():
        results = count_line(line)
        all_chars += results[0]
        all_in_memory += results[1]
    return all_chars - all_in_memory

### main 
# mode = "TEST"
mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
elif mode == "TEST":
    file = open(test_input_path)
    input = file.read()

result = count_difference(input)
result2 = count_new_len(input)

if mode == "TASK":
    print("Task 1: " + str(result))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    print("Test 2: " + str(int(test_result2) == result2) + "\n    Expected test result 2: " + str(test_result2) + "   |   Actual test result 2: " + str(result2))
print()