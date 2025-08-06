import itertools

### test cases:
test = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
test_result = """605"""

### input file path
input_path = """.\\2015\input_day09.txt""" # specific for windows

### functions and globals
locations = set()
all_possible_ways = list()

def get_all_locations(line):
    sub_line = line.split(' ')
    locations.add(sub_line[0])
    locations.add(sub_line[2])

def calc_way_length(way):
    way_len = 0
    i = 0
    for i in range(len(way)-1):
        pair = [way[i], way[i+1]]
        for line in input.splitlines():
            if pair[0] in line and pair[1] in line:
                way_len += int(line.split(' ')[4])
    return way_len 

### main 
mode = "TASK"
# mode = "TEST"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
elif mode == "TEST":
    input = test

for line in input.splitlines():
    get_all_locations(line)
all_possible_ways = list(itertools.permutations(locations, len(locations)))
results = []
i = 0
shortest_way_index = 0
longest_way_index = 0
result = []
for i in range(len(all_possible_ways)):
    current_way = calc_way_length(all_possible_ways[i])
    results.append(current_way)
    if results[shortest_way_index] > current_way:
        shortest_way_index = i
    if results[longest_way_index] < current_way:
        longest_way_index = i
print("Shortest way: " + str(results[shortest_way_index]))
print("Longest way: " + str(results[longest_way_index]))