import itertools

### test cases:
test_input = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""
test_result1 = """330"""
test_result2 = ["David",  "Alice",  "Bob",  "Carol"]

### input file path
input_path = """.\\2015\input_day13.txt""" # specific for windows

### functions
def get_all_guests_combinations(input_mood):
    guests = set()
    for line in input_mood.splitlines():
        guests.add(line.split(" ")[0])
        guests.add(line.split(" ")[10][:-1]) # [:-1] to strip the dot at the end
    return list(itertools.permutations(guests, len(guests)))
    
def get_pair_mood(name1, name2, input_mood):
    mood1 = 0
    mood2 = 0
    for line in input_mood.splitlines():
        line_list = line.split(" ")
        if name1 == line_list[0] and name2 in line_list[10]:
            mood1 = int(line_list[3])
            if line_list[2] == "lose":
                mood1 *= -1
        if name2 == line_list[0] and name1 in line_list[10]:
            mood2 = int(line_list[3])
            if line_list[2] == "lose":
                mood2 *= -1
    return mood1 + mood2
    
def combination_mood(combination, input_mood):
    mood = 0
    i = 0
    while i < len(combination):
        if i < len(combination) - 1:
            mood += get_pair_mood(combination[i], combination[i+1], input_mood)
        elif i == len(combination) - 1:
            mood += get_pair_mood(combination[i], combination[0], input_mood)
        i += 1
    return mood
    
def find_best_mood(input_mood):
    guests_combinations = get_all_guests_combinations(input_mood)
    mood = 0
    best_comb = []
    for comb in guests_combinations:
        if mood < combination_mood(comb, input_mood):
            mood = combination_mood(comb, input_mood)
            best_comb = comb
    # print(best_comb)
    # print(mood)
    return mood

### main 
# mode = "TEST"
mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
elif mode == "TEST":
    input = test_input

result = find_best_mood(input)

if mode == "TASK":
    print("Task 1: " + str(result))
    # print("Task 2: " + str(result))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result1) == result) + "\n    Expected test result 1: " + str(test_result1) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()