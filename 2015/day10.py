### test cases:
test = """1211\n111221"""
expected_test_results = """111221\n312211"""

### input
task = "1113122113"
loops_count = 50

### functions
def evaluate(number):
    i = 0
    
    #setup
    current_digit = number[i]
    digit_count = 1
    result = ""
    
    while i < len(number) -1:
        if number[i+1] == current_digit:
            digit_count += 1
        else:
            result += str(digit_count) + current_digit
            current_digit = number[i+1]
            digit_count = 1
        i += 1
    result += str(digit_count) + current_digit
    return result
    
### main 
mode = "TASK"
# mode = "TEST"

print("\nMode: " + mode)
if mode == "TASK":
    input = task
    task_result = input
    for i in range(loops_count):
        task_result = evaluate(task_result)
        if i == 39:
            print("TASK part 1 : " + str(len(task_result)))
        if i == 49:
            print("TASK part 2 : " + str(len(task_result)))
elif mode == "TEST":
    input = test.splitlines()
    test_results = []
    for numb in input:
        test_results.append(evaluate(numb))
    test_res = test_results[0] + "\n" + test_results[1]
    print("Expected test result: " + expected_test_results)
    print("Test result: " + test_res)

if mode == "TASK":
    print()
    # print("Task 1: " + str(result))
    # print("Task 2: " + str(result))
elif mode == "TEST":
    # print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
    print()
print()