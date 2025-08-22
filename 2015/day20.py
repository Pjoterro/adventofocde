import math

### test cases:
test = """150"""
test_result = """8"""

### input file path
input_path = """.\\2015\input_day20.txt""" # specific for windows

### functions
def find_elves(numb):
    factorials = set()
    i = 1
    while i < (math.sqrt(numb) + 1):
        if numb % i == 0:
            factorials.add(i)
            factorials.add(numb/i)
        i += 1
    return factorials

def find_finite_elves(numb):
    factorials = set()
    fac_1 = 1
    while fac_1 < (math.sqrt(numb) + 1):
        if numb % fac_1 == 0:
            fac_2 = numb / fac_1
            if numb / fac_1 <= 50:
                factorials.add(fac_1)
            if numb / fac_2 <= 50:
                factorials.add(fac_2)
        fac_1 += 1
    return factorials

def find_elves_number_sum(numb):
    result = []
    i = 1
    while True:
        factorial_sum = sum(find_elves(i)) * 10
        if i % 100000 == 0:
            print("Checking house no: " + str(i) + "...")
        if factorial_sum >= numb:
            result.append(i)
            break
        else:
            i += 1
    while True:
        factorial_sum = sum(find_finite_elves(i)) * 11
        if i % 100000 == 0:
            print("Checking house no: " + str(i) + "...")
        if factorial_sum >= numb:
            result.append(i)
            break
        else:
            i += 1
    return result

### main 
# mode = "TEST"
mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
elif mode == "TEST":
    input = test

result = find_elves_number_sum(int(input))

if mode == "TASK":
    print("Task 1: " + str(result[0]))
    print("Task 2: " + str(result[1]))
elif mode == "TEST":
    print()
    print("Test 1: " + str(int(test_result) == result) + "\n    Expected test result 1: " + str(test_result) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()
