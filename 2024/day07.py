import sys
import copy

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day7_input.txt"

### Start of test case ###
test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

test_1 = 3749
test_2 = 11387
### End of test case ###

def gen_input(input):
    results = []
    for line in input.splitlines():
        if line == "":
            continue
        single_res = []
        single_res.append(int(line.split(":")[0]))
        for numb in line.split(":")[1].split():
            single_res.append(int(numb))
        results.append(single_res)
    return results

def gen_op_comb(comb_len):
    result = []
    if comb_len == 1:
        result = ["+", "*", "|"]
    elif comb_len > 1:
        for op in gen_op_comb(comb_len - 1):
            result.append("+" + op)
            result.append("*" + op)
            result.append("|" + op)
    else:
        print("sth wrong with recurent func")
    return result

def is_combo_possible(num_combo, op_combo):
    num_copy = copy.deepcopy(num_combo)
    result = num_copy[0]
    num_copy.pop(0)
    for op in op_combo:
        buffor = num_copy[1]
        num_copy.pop(1)
        if op == "+":
            num_copy[0] = num_copy[0] + buffor
        elif op == "*":
            num_copy[0] = num_copy[0] * buffor
        elif op == "|":
            num_copy[0] = int(str(num_copy[0]) + str(buffor))
    return result == num_copy[0]

def is_record_possible(num_combo):
    op_combs = gen_op_comb(len(num_combo)-2)
    for op_combo in op_combs:
        if is_combo_possible(num_combo, op_combo):
            return True
    return False

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

result = 0
i = 0
m = len(gen_input(input))

for rec in gen_input(input):
    if is_record_possible(rec):
        result = result + rec[0]
    i = i + 1
    if i % 50 == 0:
        print("progress: " + str(round((i/m)*100, 2)) + "%")
print(result)

if mode == "TEST":
    print("test status: " + str(test_1 == result))
    print("test status: " + str(test_2 == result))
