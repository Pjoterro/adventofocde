### test cases:
test_input = """[1,2,3]\n{"a":2,"b":4}\n[[[3]]]{"a":{"b":4},"c":-1}{"a":[-1,1]}[-1,{"a":1}][]{}"""
test_result = """18"""

### input file path
input_path = """.\\2015\input_day12.txt""" # specific for windows

### functions
#TODO: part2

def add_one_line(line):
    num_symb = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]
    result = 0
    i = 0
    flag = False
    num_str = ""
    
    while i < len(line):
        if not flag: # we are looking for number candidate
            if line[i] in num_symb: # we found new number candidate
                flag = True
                num_str += line[i]
            # else: # still no number candidate
            #     pass
        else: # we already found number candidade
            if line[i] in num_symb: # we continue to reveal number
                num_str += line[i]
            else: # we found end of number candidade
                flag = False
                result += int(num_str)
                num_str = ""
        i += 1
    return result
    
def sum_all_file(file):
    result = 0
    for line in file.splitlines():
        result += add_one_line(line)
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

result = sum_all_file(input)

if mode == "TASK":
    print("Task 1: " + str(result))
    # print("Task 2: " + str(result))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()