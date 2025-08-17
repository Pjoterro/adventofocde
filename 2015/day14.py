### test cases:
test_input = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
test_duration = 1000
test_result1 = "Comet"
test_result2 = [1120, 1056]
test_result3 = """689"""

### input file path
input_path = """.\\2015\input_day14.txt""" # specific for windows
task_duration = 2503

### functions
#TODO: part2

def get_reindeer(input_raw):
    result = []
    for line in input_raw.splitlines():
        splitted = line.split(" ")
        reindeer = []
        reindeer.append(splitted[0])
        reindeer.append(int(splitted[3]))
        reindeer.append(int(splitted[6]))
        reindeer.append(int(splitted[13]))
        result.append(reindeer)
    return result # [name, speed, time of flight, time of rest]

def get_reindeer_v2(input_raw):
    result = []
    for line in input_raw.splitlines():
        splitted = line.split(" ")
        reindeer = []
        reindeer.append(splitted[0])
        reindeer.append(int(splitted[3]))
        reindeer.append(int(splitted[6]))
        reindeer.append(int(splitted[13]))
        reindeer.append(0)
        reindeer.append(0)
        result.append(reindeer)
    return result # [name, speed, time of flight, time of rest, current distance, score]

def evaluate_reindeer(stats, duration): # [name, speed, time of flight, time of rest]
    full_cycle_time = stats[2] + stats[3]
    cycles = int(duration/full_cycle_time)
    last_cycle = duration % full_cycle_time
    distance = stats[1]*stats[2]*cycles
    if last_cycle < stats[2]:
        distance += stats[1]*last_cycle
    else:
        distance += stats[1]*stats[2]
    return distance

def evaluate_all_by_sec(input_raw, duration):
    reindeers = get_reindeer_v2(input_raw)
    i = 0
    distances = []
    while i < duration:
        i += 1
        for rein in reindeers:
            curr_dist = evaluate_reindeer(rein, i)
            rein[4] = curr_dist
            distances.append(curr_dist)
        for rein in reindeers:
            if rein[4] == max(distances):
                rein[5] += 1
        if i == 999:
            print(distances)
        distances.clear()
    scores = []
    for rein in reindeers:
        scores.append(rein[5])
    print(scores)
    return max(scores)

def evaluate_all(input_raw, duration):
    reindeers = get_reindeer(input_raw)
    best_name = reindeers[0][0]
    best_distance = evaluate_reindeer(reindeers[0], duration)
    for r in reindeers:
        if evaluate_reindeer(r, duration) > best_distance:
            best_distance = evaluate_reindeer(r, duration)
            best_name = r[0]
    print(best_name)
    return best_distance
        
### main 
# mode = "TEST"
mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    file = open(input_path)
    input = file.read()
    duration = task_duration
elif mode == "TEST":
    input = test_input
    duration = test_duration

result = evaluate_all(input, duration)
result2 = evaluate_all_by_sec(input, duration)

if mode == "TASK":
    print("Task 1: " + str(result))
    print("Task 2: " + str(result2))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result2[0]) == result) + "\n    Expected test result 1: " + str(test_result2[0]) + "   |   Actual test result 1: " + str(result))
    print("Test 2: " + str(int(test_result3) == result2) + "\n    Expected test result 2: " + str(test_result3) + "   |   Actual test result 2: " + str(result2))
print()