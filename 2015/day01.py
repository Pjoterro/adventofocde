### test cases:
test1 = """)())())"""
test_result1 = """-3"""
test2 = """()())"""
test_result2 = """5"""

### input file path
input_path = """.\\2015\input_day01.txt"""

### functions
def resolve_floor(input):
    result = 0
    count = 0
    for character in input:
        count = count + 1
        if character == '(':
            result = result + 1
        elif character == ')':
            result = result - 1
    return result

def find_basement(input):
    result = 0
    count = 0
    for character in input:
        count = count + 1
        if character == '(':
            result = result + 1
        elif character == ')':
            result = result - 1
        if result < 0:
            return count
    print("Did not enter basement")
    return -1

### main 
# mode = "TASK"
mode = "TEST"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
elif mode == "TEST":
    input1 = test1
    input2 = test2

result1 = resolve_floor(input1)
result2 = find_basement(input2)

if mode == "TASK":
    print("Task 1: " + str(result1))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result1) == result1) + "\n    Expected test result 1: " + str(test_result1) + "   |   Actual test result 1: " + str(result1))
    print("Test 2: " + str(int(test_result2) == result2) + "\n    Expected test result 2: " + str(test_result2) + "   |   Actual test result 2: " + str(result2))
print()