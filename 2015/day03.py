### test cases:
test1 = """>"""
test_result1 = """2"""
test2 = """^>v<"""
test_result2 = """4"""
test_result22 = """3"""
test3 = """^v^v^v^v^v"""
test_result3 = """2"""
test_result32 = """11"""
test4 = """^v"""
test_result4 = """3"""

### input file path
input_path = ".\\2015\input_day03.txt"

### functions
def count_unique_houses(input):
    unique_houses = [[0, 0]] # [x, y]; [0, 0] is starting, first unique house
    pos = unique_houses[0]
    for direction in input:
        if direction == "^":
            pos = [pos[0], pos[1] + 1]
        elif direction == ">":
            pos = [pos[0] + 1, pos[1]]
        elif direction == "v":
            pos = [pos[0], pos[1] - 1]
        elif direction == "<":
            pos = [pos[0] - 1, pos[1]]
        else:
            print("Wrong parsing at:")
            print(direction)
            return -1
        if pos not in unique_houses:
            unique_houses.append(pos)
    return unique_houses

def split_input_for_robo_santa(input):
    santa_path = []
    robo_path = []
    i = 0
    for direction in input:
        if i % 2 == 0:
            santa_path.append(direction)
        elif i % 2 != 0:
            robo_path.append(direction)
        else:
            print("Wrong iterator: ")
            print(i)
            return -1
        i = i + 1
    return [santa_path, robo_path]

def get_unique_for_both(two_paths):
    santa_uniques = count_unique_houses(two_paths[0])
    robo_uniques = count_unique_houses(two_paths[1])
    for unique in santa_uniques:
        if unique in robo_uniques:
            robo_uniques.remove(unique)
    return santa_uniques + robo_uniques

### main 
mode = "TASK"
# mode = "TEST"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input1 = file.read()
    result1 = len(count_unique_houses(input1))
    result2 = len(get_unique_for_both(split_input_for_robo_santa(input1)))
elif mode == "TEST":
    input1 = test1
    input2 = test2
    input3 = test3
    input4 = test4
    result1 = len(count_unique_houses(input1))
    result2 = len(count_unique_houses(input2))
    result3 = len(count_unique_houses(input3))
    result4 = len(get_unique_for_both(split_input_for_robo_santa(input4)))
    result5 = len(get_unique_for_both(split_input_for_robo_santa(input2)))
    result6 = len(get_unique_for_both(split_input_for_robo_santa(input3)))

if mode == "TASK":
    print("Task 1: " + str(result1))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result1) == result1) + "\n    Expected test result 1: " + str(test_result1) + "   |   Actual test result 1: " + str(result1))
    print("Test 2: " + str(int(test_result2) == result2) + "\n    Expected test result 2: " + str(test_result2) + "   |   Actual test result 2: " + str(result2))
    print("Test 3: " + str(int(test_result3) == result3) + "\n    Expected test result 3: " + str(test_result3) + "   |   Actual test result 3: " + str(result3))
    print("Test 3: " + str(int(test_result4) == result4) + "\n    Expected test result 3: " + str(test_result4) + "   |   Actual test result 3: " + str(result4))
    print("Test 3: " + str(int(test_result22) == result5) + "\n    Expected test result 3: " + str(test_result22) + "   |   Actual test result 3: " + str(result5))
    print("Test 3: " + str(int(test_result32) == result6) + "\n    Expected test result 3: " + str(test_result32) + "   |   Actual test result 3: " + str(result6))
print()