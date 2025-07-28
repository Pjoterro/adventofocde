### test cases:
test = """2x3x4
1x1x10"""
test_result1 = """101"""
test_result2 = """48"""

### input file path
input_path = ".\\2015\input_day02.txt"

### functions
def get_dimensions(input):
    result = []
    for dimensions_set in input.split("\n"):
        result.append(dimensions_set.split("x"))
    return result

def single_paper(dimensions):
    result = []
    result.append(int(dimensions[0])*int(dimensions[1]))
    result.append(int(dimensions[0])*int(dimensions[2]))
    result.append(int(dimensions[1])*int(dimensions[2]))
    result = sorted(result)
    paper = 3*result[0] + 2*result[1] + 2*result[2]
    return paper

def single_ribbon(dimenions):
    result = [int(dimenions[0]), int(dimenions[1]), int(dimenions[2])]
    result = sorted(result)
    ribbon = 2*result[0] + 2*result[1] + result[0]*result[1]*result[2]
    return ribbon

def calc_whole_paper(input):
    result = 0
    for dime in get_dimensions(input):
        result = result + single_paper(dime)
    return result

def calc_whole_ribbon(input):
    result = 0
    for dime in get_dimensions(input):
        result = result + single_ribbon(dime)
    return result

### main 
mode = "TASK"
# mode = "TEST"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
elif mode == "TEST":
    input = test

result1 = calc_whole_paper(input)
result2 = calc_whole_ribbon(input)
if mode == "TASK":
    print("Task 1: " + str(result1))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result1) == result1) + "\n    Expected test result 1: " + str(test_result1) + "   |   Actual test result 1: " + str(result1))
    print("Test 2: " + str(int(test_result2) == result2) + "\n    Expected test result 2: " + str(test_result2) + "   |   Actual test result 2: " + str(result2))
print()