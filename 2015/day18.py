### test cases:
test = """
.#.#.#
...##.
#....#
..#...
#.#..#
####.."""
test_steps = """4"""
test_result1 = """......
......
..##..
..##..
......
......"""
test_result2 = """4"""

### input file path
input_path = """.\\2015\input_day18.txt""" # specific for windows
task_steps = """100"""

### functions and globals
light_map = list(list())

def parse_map(input):
    for line in input.splitlines():
        buffor = []
        for symb in line.split():
            buffor.append(symb)
        light_map.append(buffor)
    print("Map parsed!")

def get_neigbhours_coord(light_coord): # [x, y]
    map_x_size = len(light_map[0])
    map_y_size = len(light_map)
    cands = []

    cands.append([light_coord[0]-1, light_coord[1]-1])
    cands.append([light_coord[0], light_coord[1]-1])
    cands.append([light_coord[0]+1, light_coord[1]-1])

    cands.append([light_coord[0]-1, light_coord[1]])
    cands.append([light_coord[0]+1, light_coord[1]])

    cands.append([light_coord[0]-1, light_coord[1]+1])
    cands.append([light_coord[0], light_coord[1]+1])
    cands.append([light_coord[0]+1, light_coord[1]+1])

    results = []
    for coords in cands:
        if coords[0] > 0 and coords[0] < map_x_size:
            if coords[1] > 0 and coords[1] < map_y_size:
                results.append(coords)
    return results

def count_on_neighbours(light_coord): # [x, y]
    map_x_size = len(light_map[0])
    map_y_size = len(light_map)
    neigbours = get_neigbhours_coord(light_coord)
    result = 0
    for neighb in neigbours:
        if light_map[neighb[1]][neighb[0]] == "#":
            result += 1
    return result

def perform_action():
    new_map = []
    global light_map
    old_map = light_map
    for y in range(len(old_map)):
        buffer = []
        for x in range(len(old_map[y])):
            symb = ""
            if old_map[y][x] == "#" and (count_on_neighbours([x, y]) == 2 or count_on_neighbours([x, y]) == 3):
                symb = "#"
            elif old_map[y][x] == "." and count_on_neighbours([x, y]) == 3:
                symb = "#"
            else:
                symb = "."
            buffer.append(symb)
        new_map.append(buffer)
    old_map.clear()
    light_map = new_map

def count_all_lit():
    result = 0
    for y in range(len(light_map)):
        for x in range(len(light_map[y])):
            if light_map[y][x] == "#":
                result += 1
    return result

def print_map():
    global light_map
    for y in range(len(light_map)):
        buffer = ""
        for x in range(len(light_map[y])):
            buffer += light_map[y][x]
        print(buffer)

### main 
mode = "TEST"
# mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
    steps = int(task_steps)
elif mode == "TEST":
    input = test
    steps = int(test_steps)

parse_map(input)
i = 0
while i < steps:
    perform_action()
    print_map()
    i += 1
result = count_all_lit()


if mode == "TASK":
    print("Task 1: " + str(result))
    # print("Task 2: " + str(result))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result2) == result) + "\n    Expected test result 1: " + str(test_result2) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()