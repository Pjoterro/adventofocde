### test cases:
test_input = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 168 seconds."""
test_duration = 1000
test_result1 = "Dancer"
test_result2 = [1120, 1056]

### input file path
input_path = """.\\2015\input_day14.txt""" # specific for windows
task_duration = 2503

### functions
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

if mode == "TASK":
    print("Task 1: " + str(result))
    # print("Task 2: " + str(result))
elif mode == "TEST":
    print("Test 1: " + str(int(test_result2[1]) == result) + "\n    Expected test result 1: " + str(test_result2[1]) + "   |   Actual test result 1: " + str(result))
    # print("Test 2: " + str(int(test_result) == result) + "\n    Expected test result 2: " + str(test_result) + "   |   Actual test result 2: " + str(result))
print()