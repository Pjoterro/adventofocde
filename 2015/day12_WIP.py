test_input = """[1,2,3]\n{"a":2,"b":4}\n[[[3]]]{"a":{"b":4},"c":-1}{"a":[-1,1]}[-1,{"a":1}][]{}"""
test_result = """18"""

num_symb = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]

def add_one_line(line):
    result = 0
    i = 0
    flag = False
    num_str = ""
    
    while i < len(line):
        # print(line[i] + "| " + str(result) + " | " + str(i) + " | " + str(flag) + " | " + str(num_str))
        if not flag: # we are looking for numb candidate
            if line[i] in num_symb: # we found new numb candidate
                flag = True
                num_str += line[i]
            # else: # still no numb candidate
            #     pass
        else: # we already found numb candidade
            if line[i] in num_symb: # we continue to reveal numb
                num_str += line[i]
            else: # we found end of numb candidade
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
    
print(sum_all_file(test_input))
