### test cases:
test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
test_result_1 = """1227775554"""
test_result_2 = """4174379265"""

### input file path
input_path = """.\\2025\inputs\input_day_02.txt""" # specific for windows

### functions
def find_invalid_id(input):
    result = []
    for pair in input.split(','):
        start = int(pair.split('-')[0])
        end = int(pair.split('-')[1])
        i = start
        while i <= end:
            if len(str(i)) % 2 == 0:
                if str(i)[0:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
                    result.append(i)
            i += 1
    return result

def find_invalid_id_v2(input):
    result = []
    for pair in input.split(','):
        start = int(pair.split('-')[0])
        end = int(pair.split('-')[1])
        i = start
        while i <= end:
            dividers = []
            for j in range(1, int(len(str(i))/2) + 1):
                if len(str(i)) % j == 0:
                    dividers.append(j)
            for divider in dividers:
                parts = []
                valid_flag = True
                for k in range(int(len(str(i))/divider)):
                     parts.append(str(i)[0+k*divider:divider+k*divider])
                for k in range(len(parts)-1):
                    if not parts[k] == parts[k+1] and len(parts) > 1:
                        valid_flag = False
                        break
                if valid_flag:
                    result.append(i)
                    break
            i += 1
    return result

def count_invalid_id(input):
    result = 0
    for id in find_invalid_id(input):
        result += id
    return result

def count_invalid_id_v2(input):
    result = 0
    for id in find_invalid_id_v2(input):
        result += id
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

print("Part I started...")
result_1 = count_invalid_id(input)
print("Part I ended!")
print("Part II started...")
result_2 = count_invalid_id_v2(input)
print("Part II ended!")

if mode == "TEST":
    print("Test 1: " + str(int(test_result_1) == result_1) + "\n    Expected test result 1: " + str(test_result_1) + "   |   Actual test result 1: " + str(result_1))
    print("Test 2: " + str(int(test_result_2) == result_2) + "\n    Expected test result 2: " + str(test_result_2) + "   |   Actual test result 2: " + str(result_2))
elif mode == "TASK":
    print("Task 1: " + str(result_1))
    print("Task 2: " + str(result_2))
print()