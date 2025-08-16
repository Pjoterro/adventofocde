### test cases:
test_input = """[1,2,3]{"a":2,"b":4}[[[3]]]{"a":{"b":4},"c":-1}{"a":[-1,1]}[-1,{"a":1}][]{}"""
test_result = """18"""
test_input_2 = """[1,2,3][1,{"c":"red","b":2},3]{"d":"red","e":[1,2,3,4],"f":5}[1,"red",5]"""
test_result_2 = """16"""

### input file path
input_path = """.\\2015\input_day12.txt""" # specific for windows

### functions
def assess_bracket(bracket):
    result = 0
    has_red = check_for_red(bracket)
    subrackets = get_subbrackets(bracket)
    if has_red:
        result = 0
    else:
        result = sum_bracket(bracket)
        if len(subrackets) > 0:
            for subbracket in subrackets:
                result += assess_bracket(subbracket)
    return result
    
def check_for_red(bracket):
    i = 0
    current_level = 0
    if bracket[0] == "[":
        return False
    while i < len(bracket):
        if bracket[i] == "r" and current_level == 1:
            if bracket[i+1] == "e" and bracket[i+2] == "d":
                return True
        elif bracket[i] == "[" or bracket[i] == "{":
            current_level += 1
        elif bracket[i] == "]" or bracket[i] == "}":
            current_level -= 1
        i += 1
    return False
    
def get_subbrackets(bracket):
    result = []
    i = 0
    current_level = 0
    buffor = ""
    while i < len(bracket):
        if bracket[i] == "[" or bracket[i] == "{":
            current_level += 1
        elif bracket[i] == "]" or bracket[i] == "}":
            current_level -= 1
            if current_level == 1:
                buffor += bracket[i]
                result.append(buffor)
                buffor = ""
        if current_level > 1:
            buffor += bracket[i]
        i += 1
    return result
    
def sum_bracket(bracket):
    num_symb = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]
    result = 0
    i = 0
    num_flag = False
    current_level = 0
    num_str = ""
    while i < len(bracket):
        if bracket[i] == "[" or bracket[i] == "{":
            current_level += 1
        elif current_level == 1:
            if not num_flag:
                if bracket[i] in num_symb:
                    num_flag = True
                    num_str += bracket[i] 
            else:
                if bracket[i] in num_symb:
                    num_str += bracket[i]
                else:
                    num_flag = False
                    result += int(num_str)
                    num_str = ""
        elif bracket[i] == "]" or bracket [i] == "}":
            current_level -= 1
        i += 1
    return result

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
    input2 = test_input_2

result = sum_all_file(input)
result2 = assess_bracket(input)

if mode == "TASK":
    print("Task 1: " + str(result))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    print("Test 2: " + str(int(test_result_2) == result2) + "\n    Expected test result 2: " + str(test_result_2) + "   |   Actual test result 2: " + str(result2))
print()
