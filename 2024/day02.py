import sys
mode = sys.argv[1] # TEST or TASK
input_file_path = "./day2_input.txt"

### Start of test case ###
test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
48 46 47 49 51 54 56
1 1 2 3 4 5
1 2 3 4 5 5
5 1 2 3 4 5
1 4 3 2 1
1 6 7 8 9
1 2 3 4 3
9 8 7 6 7
7 10 8 10 11
29 28 27 25 26 25 22 20"""

test_safe = 2
test_safe2 = 14
### End of test case ###

def define_ascending_modifier(record):
    plus_count = 0
    minus_count = 0
    for i in range(len(record) -1):
        delta = (int(record[i+1]) - int(record[i]))
        if delta > 0:
            plus_count = plus_count + 1
        if delta < 0:
            minus_count = minus_count + 1
    if plus_count > minus_count:
        return 1
    else:
        return -1
    
def is_record_safe(record): # must be already seperated!
    res_bool = True
    res_index = -1
    asc_mod = define_ascending_modifier(record)
    for i in range(len(record) -1):
        delta = (int(record[i+1]) - int(record[i])) * asc_mod
        if (delta < 1 or delta > 3):
            res_index = i
            res_bool = False
            break
    result = {"is_safe": res_bool, "index": res_index}
    return result
    
def is_record_safe_broad(record):
    first_pass = is_record_safe(record)
    if first_pass["is_safe"] == True:
        return True
    else:
        subrecords = []
        
        if first_pass["index"] >= 1:
            subrec0 = record.copy()
            subrec0.pop(first_pass["index"] - 1)
            subrecords.append(subrec0)
            
        subrec1 = record.copy()
        subrec1.pop(first_pass["index"])
        subrecords.append(subrec1)
        
        subrec2 = record.copy()
        subrec2.pop(first_pass["index"] + 1)
        subrecords.append(subrec2)
        
        for subrecord in subrecords:
            subresult = is_record_safe(subrecord)
            if subresult["is_safe"] == True:
                return True
        return False
            
def filter_safe_results(all_results):
    results = []
    for line in all_results.splitlines():
        if (line == ""):
            continue
        if is_record_safe_broad(line.split()):
            results.append(line)
    return results


### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

buffer = filter_safe_results(input)
print("no. of safe reports: " + str(len(buffer)))
if mode == "TEST":
    print("test status: " + str(len(buffer) == test_safe2))
