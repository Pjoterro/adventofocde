import sys
import re

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day3_input.txt"

### Start of test case ###
test_input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

test_mul = 161
test_mul2 = 48
### End of test case ###

mul_reg = r'mul\(\d+,\d+\)'
dont_do_reg = r'don\'t\(\).*do\(\)'
do_reg = r'do\(\)'
dont_reg = r'don\'t\(\)'
mul_dont_do_reg = r'(mul\(\d+,\d+\)|don\'t\(\)|do\(\))'

def multiply(single_mul): #w formacie string = "mul(int1,int2)"
    mul_red = single_mul.replace('mul(', '').replace(')', '')
    mul_array = mul_red.split(',')
    return int(mul_array[0])*int(mul_array[1])

def get_all_muls(input_text):
    result = re.findall(mul_reg, input_text)
    return result

def get_do_and_muls(input_text):
    result = []
    for line in input_text.splitlines():
        result.append(re.findall(mul_dont_do_reg, line))
    return result

def get_only_do_muls(input_array_of_arrays):
    result = []
    do_flag = True
    for array in input_array_of_arrays:
        for record in array:
            if do_flag:
                if "mul(" in record:
                    print("MUL found")
                    result.append(record)
                elif "don't(" in record:
                    print("DON'T found")
                    do_flag = False
            else:
                if "do(" in record:
                    print("DO found")
                    do_flag = True
        print("NEW LINE")
    return result

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

buffer = get_do_and_muls(input)
buffer = get_only_do_muls(buffer)
res = 0
for record in buffer:
    res = res + multiply(record)
print("mul result: " + str(res))
if mode == "TEST":
    print("test status: " + str(res == test_mul2))
