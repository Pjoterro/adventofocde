import sys
import copy

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day11_input.txt"

### Start of test case ###
test_input = """125 17"""

test_1 = 55312
### End of test case ###

stones = []
stones2 = {}

def input_to_stones(input):
    global stones
    for stone in input.split():
        stones.append(int(stone))
#    print(stones)

def input_to_stones2(input):
    global stones2
    for stone in input.split():
        if not stone in stones2:
            stones2[stone] = 1
        else:
            stones2.update({stone : stones2.get(stone) + 1})

def blink():
    global stones2
    next_step = {}
    next_step.clear()
    for stone in stones2:
        amount = stones2.get(stone)
        if int(stone) == 0:
            if 1 in next_step:
                next_step.update({1 : next_step.get(1) + amount})
            else:
                next_step[1] = amount
        elif len(str(stone))%2 == 0:
            #print("stone length: " + str(len(str(stone))))
            part1 = ''
            part2 = ''
            for i in range(0, len(str(stone))):
                if i < len(str(stone))/2:
                    part1 = part1 + str(stone)[i]
                else:
                    part2 = part2 + str(stone)[i]
            if int(part1) in next_step:
                next_step.update({int(part1) : next_step.get(int(part1)) + amount})
            else:
                next_step[int(part1)] = amount
            if int(part2) in next_step:
                next_step.update({int(part2) : next_step.get(int(part2)) + amount})
            else:
                next_step[int(part2)] = amount
        else:
            if int(stone)*2024 in next_step:
                next_step.update({int(stone)*2024 : next_step.get(int(stone)*2024) + amount})
            else:
                next_step[int(stone)*2024] = amount
    stones2.clear()
    stones2 = next_step
    count_stones2()

def count_stones2():
    global stones2
    stones_amount = 0
    distinct_stones = 0
    for stone in stones2:
        stones_amount = stones_amount + int(stones2[stone])
        distinct_stones = distinct_stones + 1
#    print("distinct stones: " + str(distinct_stones) + " | total amount: " + str(stones_amount))
    return stones_amount

def evaluate_step_bf():
    global stones
    next_step = []
    for stone in stones:
        if stone == 0:
            next_step.append(1)
        elif len(str(stone))%2 == 0:
            part1 = ''
            part2 = ''
            for i in range(0, len(str(stone))):
                if i < len(str(stone))/2:
                    part1 = part1 + str(stone)[i]
                else:
                    part2 = part2 + str(stone)[i]
            next_step.append(int(part1))
            next_step.append(int(part2))
        else:
            next_step.append(stone*2024)
    stones = next_step

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

input_to_stones(input)
input_to_stones2(input)


for i in range(0, 75):
#    evaluate_step_bf()
    print("blink no. " + str(i+1))
    blink()

result = count_stones2()
print(str(result))

if mode == "TEST":
    print("test status: " + str(test_1 == result))
#    print("test status: " + str(test_2 == buffor3))
