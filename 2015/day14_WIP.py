test_input = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 168 seconds."""
test_duration = 1000
test_result = [1120, 1056]

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
    for r in reindeers:
        print(r[0])
        print(evaluate_reindeer(r, duration))

evaluate_all(test_input, test_duration)
