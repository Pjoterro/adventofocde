import sys
import copy

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day10_input.txt"

### Start of test case ###
test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

test_1 = 36
test_2 = 81
### End of test case ###

map = []

def input_to_2darray(input):
    global map
    for line in input.splitlines():
        map_line = []
        if line == "":
            continue
        for char in line:
            map_line.append(int(char))
        map.append(map_line)

def find_every_zero():
    global map
    result = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                result.append([x, y])
    return result

def trail_till_nine(el_cords):
    global map
    result = []
    el_val = map[el_cords[1]][el_cords[0]]

    p1 = [el_cords[0] + 1, el_cords[1]]
    p2 = [el_cords[0], el_cords[1] - 1]
    p3 = [el_cords[0] - 1, el_cords[1]]
    p4 = [el_cords[0], el_cords[1] + 1]
    neighbours = [p1, p2, p3, p4]

    for p in neighbours:
        if is_in_bounds(p) and map[p[1]][p[0]] == el_val + 1:
            if (el_val + 1 == 9) and (not p in result):
                result.append(p)
            else:
                result = result + trail_till_nine(p)
# return is depended which part of the task we are doing
#    return remove_dups(result)
    return result

def remove_dups(array):
    result = []
    for item in array:
        if not item in result:
            result.append(item)
    return result

def is_in_bounds(el_cords):
    global map
    is_x = el_cords[0] >= 0 and el_cords[0] < len(map[1])
    is_y = el_cords[1] >= 0 and el_cords[1] < len(map)
    return is_x and is_y

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

input_to_2darray(input)
result1 = 0
for zero in find_every_zero():
    print(trail_till_nine(zero))
    result1 = result1 + len(trail_till_nine(zero))
print("result1: " + str(result1))

if mode == "TEST":
    print("test status: " + str(test_2 == result1))
#    print("test status: " + str(test_2 == buffor3))
