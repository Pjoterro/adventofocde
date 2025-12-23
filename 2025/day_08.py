### test cases:
test_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
test_result_1 = """40"""
test_result_2 = """"""

### input file path
input_path = """.\\2025\inputs\input_day_08.txt""" # specific for windows

### functions
def distance_sq_between_two_points(point1, point2):
    dist_sq = (point1[0]-point2[0])*(point1[0]-point2[0]) + (point1[1]-point2[1])*(point1[1]-point2[1]) + (point1[2]-point2[2])*(point1[2]-point2[2])
    return (dist_sq, [point1, point2])

def parse_input(input):
    result = []
    for line in input.splitlines():
        point = []
        for cord in line.split(','):
            point.append(int(cord))
        result.append(point)
    return result

def calc_all_connections_length(input):
    parsed = parse_input(input)
    result = []
    for x in range(len(parsed)):
        for y in range(x+1, len(parsed)):
            result.append(distance_sq_between_two_points(parsed[x], parsed[y]))
    return result

def get_only_shortest(pairs, number):
    pairs = sorted(pairs)
    return pairs[:number]

def group_pairs(pairs):
    starting = pairs
    result = []
    flag = True
    while flag:
        flag = False
        result = [[starting[1][1][0], starting[1][1][1]]]
        for pair in starting:
            for group in result:
                if pair[1][0] in group or pair[1][1] in group:
                    group.append(pair[1][0])
                    group.append(pair[1][1])
                    flag = True
                    break
                else:
                    new_group = []
                    new_group.append(pair[1][0])
                    new_group.append(pair[1][1])
                    result.append(new_group)
                    flag = True
                    break
        if flag:
            starting = result.copy()
            result.clear()
    return result


def TEMPLATE_1(input):
    pass

def TEMPLATE_2(input):
    pass

### main 
mode = "TEST"
# mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
    number = 1000
elif mode == "TEST":
    input = test_input
    number = 10

print("Part I started...")
pairs = calc_all_connections_length(input)
result_1 = group_pairs(get_only_shortest(pairs, number))
print("Part I ended!")
print("Part II started...")
result_2 = TEMPLATE_2(input)
print("Part II ended!")

if mode == "TEST":
    print("Test 1: " + str(int(test_result_1) == result_1) + "\n    Expected test result 1: " + str(test_result_1) + "   |   Actual test result 1: " + str(result_1))
    print("Test 2: " + str(int(test_result_2) == result_2) + "\n    Expected test result 2: " + str(test_result_2) + "   |   Actual test result 2: " + str(result_2))
elif mode == "TASK":
    print("Task 1: " + str(result_1))
    print("Task 2: " + str(result_2))
print()