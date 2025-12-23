### test cases:
test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""
test_result_1 = """357"""
test_result_2 = """3121910778619"""

### input file path
input_path = """.\\2025\inputs\input_day_03.txt""" # specific for windows

### functions
def find_joltage(input):
    result = 0
    for line in input.splitlines():
        highest_first_digit = 0
        for i in range(len(line)-1):
            if int(line[i]) > int(line[highest_first_digit]):
                highest_first_digit = i
        second_highest_digit = highest_first_digit+1
        for j in range(second_highest_digit, len(line)):
            if int(line[j]) > int(line[second_highest_digit]):
                second_highest_digit = j
        result += int(line[highest_first_digit] + line[second_highest_digit])
    return result

def better_joltage_finder(single_line, digits_count):
    highest_digit = 0
    for i in range(len(single_line) - digits_count + 1):
        if int(single_line[i]) > int(single_line[highest_digit]):
            highest_digit = i
    if digits_count > 1:
        return single_line[highest_digit] + better_joltage_finder(single_line[highest_digit+1:], digits_count-1)
    elif digits_count == 1:
        return single_line[highest_digit]
    
def better_find_joltage(input):
    result = 0
    for line in input.splitlines():
        next = int(better_joltage_finder(line, 12))
        # print(next)
        result += next
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
result_1 = find_joltage(input)
print("Part I ended!")
print("Part II started...")
result_2 = better_find_joltage(input)
print("Part II ended!")

if mode == "TEST":
    print("Test 1: " + str(int(test_result_1) == result_1) + "\n    Expected test result 1: " + str(test_result_1) + "   |   Actual test result 1: " + str(result_1))
    print("Test 2: " + str(int(test_result_2) == result_2) + "\n    Expected test result 2: " + str(test_result_2) + "   |   Actual test result 2: " + str(result_2))
elif mode == "TASK":
    print("Task 1: " + str(result_1))
    print("Task 2: " + str(result_2))
print()