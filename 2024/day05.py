import sys

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day5_input.txt"

### Start of test case ###
test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

test_1 = 143
test_2 = 123
### End of test case ###

rules = []
updates = []

def split_input(raw_input):
    global rules
    global updates
    flag = True
    for line in input.splitlines():
        if flag:
            if line == "":
                flag = False
            else:
                rules.append(line)
        else:
            updates.append(line.split(','))

def is_update_correct(update):
    global rules
    for i in range(len(update) - 1):
        buffor = update[i] + '|' + update[i+1]
        if (buffor not in rules):
            return False
    return True

def sort_wrong_update_and_get_mid(update):
    global rules
    flag = True
    while flag:
        flag = False
        for i in range(len(update) - 1):
            buffor = update[i] + '|' + update[i+1]
            if (buffor not in rules):
                x = update[i]
                update[i] = update[i+1]
                update[i+1] = x
                flag = True
    return int(update[int(len(update)/2)])

def get_middle_record(update):
    return int(update[int(len(update)/2)])


### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

split_input(input)

result1 = 0
result2 = 0
for update in updates:
    if is_update_correct(update):
        result1 = result1 + get_middle_record(update)
    else:
        result2 = result2 + sort_wrong_update_and_get_mid(update)
print("result 1: " + str(result1))
print("result 2: " + str(result2))

if mode == "TEST":
    print("test status: " + str(result1 == test_1))
    print("test status: " + str(result2 == test_2))
