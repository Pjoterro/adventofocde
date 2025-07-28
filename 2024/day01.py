### Start of test case ###
test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

test_distance = 11
test_similarity_score = 31
### End of test case ###

import sys

mode = sys.argv[1] #TEST or TASK
table_left = []
table_right = []
distance = 0
similarity_score = 0
input_path = "./day1_input.txt"

def input_to_tables(input):
    for line in input.splitlines():
        if (line == ""):
            continue
        buffor = line.split()
        table_left.append(int(buffor[0]))
        table_right.append(int(buffor[1]))
    
def evaluate_distance(table_left, table_right):
    result = 0
    for i in range(len(table_left)):
        buffor = (table_left[i]) - (table_right[i])
        if buffor < 0:
            buffor = -buffor
        result = result + buffor
    return result

def reduced_dictionary(table):
    table.sort()
    result_dict = {}
    key = table[0]
    count = 0
    
    table.sort()
    for i in range(len(table)):
        if (key == table[i]):
            count = count+1
        if (key != table[i]):
            result_dict[key] = count
            key = table[i]
            count = 1
    print(result_dict)
    return result_dict

def evaluate_similarity(table_left, dict_right):
    result = 0
    for record in table_left:
        if record in dict_right:
            result = result + record * dict_right[record]
        else:
            result = result + 0
    return result

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_path)
    input = file.read()
    
input_to_tables(input)
table_left.sort()
table_right.sort()
distance = evaluate_distance(table_left, table_right)

print("distance: " + str(distance))
if mode == "TEST":
    print("test status: " + str(distance == test_distance))

right_dict = reduced_dictionary(table_right)
similarity = evaluate_similarity(table_left, right_dict)
print("similarity: " + str(similarity))
if mode == "TEST":
    print("test status: " + str(similarity == test_similarity_score))
