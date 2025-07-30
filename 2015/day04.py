import hashlib

### test cases:
test1 = """abcdef"""
test_result1 = """609043"""
test2 = """pqrstuv"""
test_result2 = """1048970"""

### input file path
input_path = ".\\2015\input_day04.txt"

### functions
def get_md5_hash(input): # simple string as input
    input_encoded = input.encode()
    hash_object = hashlib.md5(input_encoded)
    hash_key = hash_object.hexdigest()
    return hash_key # simple string as output

def look_for_five_0s(input):
    i = 0
    while True:
        buffor = input + str(i)
        hash_key = get_md5_hash(buffor)
        if hash_key[:5] == "00000":
            return i
        i = i+1

def look_for_six_0s(input):
    i = 0
    while True:
        buffor = input + str(i)
        hash_key = get_md5_hash(buffor)
        if hash_key[:6] == "000000":
            return i
        i = i+1
        

### main 
mode = "TASK"
# mode = "TEST"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
    result1 = look_for_five_0s(input)
    result2 = look_for_six_0s(input)

elif mode == "TEST":
    input1 = test1
    input2 = test2
    result1 = look_for_five_0s(input1)
    result2 = look_for_five_0s(input2)

if mode == "TASK":
    print("Task 1: " + str(result1))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    pass
    print("Test 1: " + str(int(test_result1) == result1) + "\n    Expected test result 1: " + str(test_result1) + "   |   Actual test result 1: " + str(result1))
    print("Test 2: " + str(int(test_result2) == result2) + "\n    Expected test result 2: " + str(test_result2) + "   |   Actual test result 2: " + str(result2))
print()