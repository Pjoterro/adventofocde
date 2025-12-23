### test cases:
test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
test_result_1 = """4277556"""
test_result_2 = """3263827"""

### input file path
input_path = """.\\2025\inputs\input_day_06.txt""" # specific for windows

### functions
def split_input(input):
    output = []
    new_line = []
    for line in input.splitlines():
        new_line = []
        for element in line.split():
            if element != "+" and element != '*':
                element = int(element)
            new_line.append(element)
        output.append(new_line)
    return output

def split_input_vertically(input):
    input_by_line = input.splitlines()
    output = []
    single_record = []
    for x in range(len(input_by_line[0])):
        if input_by_line[0][x] == ' ' and input_by_line[1][x] == ' ' and input_by_line[2][x] == ' ' and input_by_line[3][x] == ' ' and input_by_line[4][x] == ' ':
            output.append(single_record)
            single_record = []
        else:
            if input_by_line[-1][x] != ' ':
                single_record.append(input_by_line[-1][x])
            number = int(input_by_line[0][x] + input_by_line[1][x] + input_by_line[2][x] + input_by_line[3][x])
            single_record.append(number)
    output.append(single_record)
    return output
            
def evaluate_records(input):
    records = split_input_vertically(input)
    result = 0
    for rec in records:
        if rec[0] == '+':
            res_rec = 0
            for num in rec[1:]:
                res_rec += num
        if rec[0] == '*':
            res_rec = 1
            for num in rec[1:]:
                res_rec *= num
        result += res_rec
    return result

def count_v1(input):
    usage_data = split_input(input)
    result = 0
    for x in range(len(usage_data[0])):
        if usage_data[-1][x] == '+':
            line_result = 0
            for y in range(len(usage_data) - 1):
                line_result += usage_data[y][x]
        if usage_data[-1][x] == '*':
            line_result = 1
            for y in range(len(usage_data) - 1):
                line_result *= usage_data[y][x]
        result += line_result
    return result

def TEMPLATE_2(input):
    pass

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
result_1 = count_v1(input)
print("Part I ended!")
print("Part II started...")
result_2 = evaluate_records(input)
print("Part II ended!")

if mode == "TEST":
    print("Test 1: " + str(int(test_result_1) == result_1) + "\n    Expected test result 1: " + str(test_result_1) + "   |   Actual test result 1: " + str(result_1))
    print("Test 2: " + str(int(test_result_2) == result_2) + "\n    Expected test result 2: " + str(test_result_2) + "   |   Actual test result 2: " + str(result_2))
elif mode == "TASK":
    print("Task 1: " + str(result_1))
    print("Task 2: " + str(result_2))
print()