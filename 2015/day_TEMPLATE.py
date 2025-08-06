### test cases:
test = """"""
test_result = """"""

### input file path
input_path = """.\\2015\input_day_TEMPLATE.txt""" # specific for windows

### functions
def TEMPLATE(input):
    pass

### main 
mode = "TEST"
# mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
elif mode == "TEST":
    input = test

result = TEMPLATE(input)

if mode == "TASK":
    print("Task 1: " + str(result))
    # print("Task 2: " + str(result))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()