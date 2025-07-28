import sys
import copy

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day8_input.txt"

### Start of test case ###
test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

test_1 = 14
test_2 = 34
### End of test case ###

antena_map = []
map_size = [0, 0]

def input_to_2darray(input):
    global antena_map
    for line in input.splitlines():
        if line == "":
            continue
        res_line = []
        for x in line:
            res_line.append(x)
        antena_map.append(res_line)
    map_size[0] = len(antena_map[0])
    map_size[1] = len(antena_map)
    print("map_size[x, y]: " + str(map_size))

def get_all_antenas(): # return [A, B, C...]
    global antena_map
    global map_size
    antena_type = []
    for y in range(map_size[1]):
        for x in range(map_size[0]):
            if (not antena_map[y][x] == '.') and (antena_map[y][x] not in antena_type):
                antena_type.append(antena_map[y][x])
    return antena_type

def get_all_antena_cord(antena_type): # [[x1, y1], [x2, y2]...]
    global antena_map
    antena_cord = []
    for y in range(len(antena_map)):
        for x in range(len(antena_map[y])):
            if antena_map[y][x] == antena_type:
                antena_cord.append([x, y])
    return antena_cord

def calc_antena_inter(antena_type): # [[x1, y1], [x2, y2]...]
    global antena_map
    all_antena_cord = get_all_antena_cord(antena_type)
    antena_inter = []
    for a1 in range(len(all_antena_cord)):
        for a2 in range(a1+1, len(all_antena_cord)):
            dx = all_antena_cord[a2][0] - all_antena_cord[a1][0]
            dy = all_antena_cord[a2][1] - all_antena_cord[a1][1]
            inter1 = [all_antena_cord[a2][0] + dx, all_antena_cord[a2][1] + dy]
            inter2 = [all_antena_cord[a1][0] - dx, all_antena_cord[a1][1] - dy]
            if is_on_map(inter1):
                antena_inter.append(inter1)
            if is_on_map(inter2):
                antena_inter.append(inter2)
    return antena_inter

def calc_antena_inter_harmonic(antena_type): # [[x1, y1], [x2, y2]...]
    global antena_map
    all_antena_cord = get_all_antena_cord(antena_type)
    antena_inter = []
    for a1 in range(len(all_antena_cord)):
        for a2 in range(a1+1, len(all_antena_cord)):
            dx = all_antena_cord[a2][0] - all_antena_cord[a1][0]
            dy = all_antena_cord[a2][1] - all_antena_cord[a1][1]
            inter_flag = True
            inter = [all_antena_cord[a2][0], all_antena_cord[a2][1]]
            while inter_flag:
                if is_on_map(inter):
                    antena_inter.append(copy.deepcopy(inter))
                    inter[0] = inter[0] + dx
                    inter[1] = inter[1] + dy
                else:
                    inter_flag = False
                    break
            inter_flag = True
            inter = [all_antena_cord[a1][0], all_antena_cord[a1][1]]
            while inter_flag:
                if is_on_map(inter):
                    antena_inter.append(copy.deepcopy(inter))
                    inter[0] = inter[0] - dx
                    inter[1] = inter[1] - dy
                else:
                    inter_flag = False
                    break
    return antena_inter


def is_on_map(inter):
    global map_size
    is_x_on_map = inter[0] >= 0 and inter[0] < map_size[0]
    is_y_on_map = inter[1] >= 0 and inter[1] < map_size[1]
    return is_x_on_map and is_y_on_map

def get_inter_amount():
    all_unique_inter = []
    for antena in get_all_antenas():
        antena_inter = calc_antena_inter(antena)
        for inter in antena_inter:
            if inter not in all_unique_inter:
                all_unique_inter.append(inter)
    return len(all_unique_inter)

def get_inter_amount_harmonic():
    all_unique_inter = []
    for antena in get_all_antenas():
        antena_inter = calc_antena_inter_harmonic(antena)
        for inter in antena_inter:
            if inter not in all_unique_inter:
                all_unique_inter.append(inter)
    return len(all_unique_inter)

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

input_to_2darray(input)

buffor = get_inter_amount()
print("buffor: " + str(buffor))

buffer2 = get_inter_amount_harmonic()
print("buffer2: " + str(buffer2))

if mode == "TEST":
    print("test status: " + str(test_1 == buffor))
    print("test status: " + str(test_2 == buffer2))
