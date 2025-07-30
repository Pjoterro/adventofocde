### test cases:
test1 = """ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb"""
test_result1 = """2"""

### input file path
input_path = ".\\2015\input_day05.txt"

### functions
def has_3_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in word:
        if letter in vowels:
            count = count + 1
            if count >= 3:
                return True
    return False    

def has_double_letter(word):
    i = 0
    for letter in word[1:]:
        if letter == word[i]:
            return True
        i = i + 1
    return False

def has_no_forbidden(word):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for forb in forbidden:
        if forb in word:
            return False
    return True

def is_nice(word):
    bool1 = has_3_vowels(word)
    bool2 = has_double_letter(word)
    bool3 = has_no_forbidden(word)
    return bool1 and bool2 and bool3

def check_list(input):
    result = 0
    for word in input.split("\n"):
        if is_nice(word):
            result = result + 1
    return result

### main 
mode = "TASK"
# mode = "TEST"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
    result1 = check_list(input)

elif mode == "TEST":
    input = test1
    result1 = check_list(input)

if mode == "TASK":
    print("Task 1: " + str(result1))
    # print("Task 2: " + str(result2))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result1) == result1) + "\n    Expected test result 1: " + str(test_result1) + "   |   Actual test result 1: " + str(result1))
    # print("Test 2: " + str(int(test_result2) == result2) + "\n    Expected test result 2: " + str(test_result2) + "   |   Actual test result 2: " + str(result2))
print()