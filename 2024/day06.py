import sys
import copy

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day6_input.txt"

### Start of test case ###
test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

test_1 = 41
test_2 = 6
### End of test case ###

input_map = []
map_size = [0, 0]
starting_pos = [0, 0, 0]
all_dir = ['^', '>', 'v', '<'] # in that order

def gen_inputs(text_input):
    global input_map
    global map_size
    global starting_pos
    for line in text_input.splitlines():
        line_arr = []
        for char in line:
            line_arr.append(char)
        input_map.append(line_arr)
    map_size[0] = len(input_map[1])
    map_size[1] = len(input_map)
    starting_pos[2] = 0
    for y in range(len(input_map)):
        for x in range(len(input_map[y])):
            if input_map[y][x] == all_dir[starting_pos[2]]:
                starting_pos[0] = x
                starting_pos[1] = y

def is_guard_at_border(curr_pos):
    global map_size
    return (curr_pos[0] == 0) or (curr_pos[0] == map_size[0]-1) or (curr_pos[1] == 0) or (curr_pos[1] == map_size[1]-1)

def get_next_pos(curr_pos):
    next_pos = curr_pos.copy()
    if next_pos[2] == 0:
        next_pos[1] = curr_pos[1] - 1
    if next_pos[2] == 1:
        next_pos[0] = curr_pos[0] + 1
    if next_pos[2] == 2:
        next_pos[1] = curr_pos[1] + 1
    if next_pos[2] == 3:
        next_pos[0] = curr_pos[0] - 1
    return next_pos

def is_possible_to_exit(map_in):
    global starting_pos
    global all_dir
    guard_path = []
    map_copy = copy.deepcopy(map_in)
    current_pos = copy.deepcopy(starting_pos)
    while not is_guard_at_border(current_pos):
        map_copy[current_pos[1]][current_pos[0]] = 'X'
        if current_pos not in guard_path:
            guard_path.append(current_pos.copy())
        else:
            return [map_copy, False]
        next_pos = get_next_pos(current_pos)
        next_pos_char = map_copy[next_pos[1]][next_pos[0]]
        if next_pos_char == '.' or next_pos_char == 'X':
            current_pos = next_pos
        elif next_pos_char == '#':
            current_pos[2] = (current_pos[2] + 1) % 4
    map_copy[current_pos[1]][current_pos[0]] = 'X'
    return [map_copy, True]

def return_path(map_in):
    global map_size
    result = []
    for y in range(map_size[1]):
        for x in range(map_size[0]):
            if map_in[y][x] == 'X':
                result.append([x, y])
    return result

def search_for_loops(path):
    global map_size
    global input_map
    global starting_pos
    results = []
    cases_to_check = len(path)
    #print("cases to check: " + str(cases_to_check))
    i = 0
    for cord in path:
        i = i+1
        working_map = copy.deepcopy(input_map)
        if cord[0] == starting_pos[0] and cord[1] == starting_pos[1]:
            continue
        else:
            working_map[cord[1]][cord[0]] = "#"
            if not is_possible_to_exit(working_map)[1]:
                results.append(cord)
            working_map.clear()
        if i % 10 == 0:
            done_percentage = (i / cases_to_check)*100
            print("progress: " + str(round(done_percentage, 2)) + "%")
    return results

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

gen_inputs(input)
buffor_map = is_possible_to_exit(input_map)[0]
path = return_path(buffor_map)
print("path len: " + str(len(path)))
obstacles = search_for_loops(path)
print("obstacles len: " + str(len(obstacles)))

if mode == "TEST":
    pass
    print("test status: " + str(test_1 == len(path)))
    print("test status: " + str(test_2 == len(obstacles)))
