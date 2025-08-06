### test cases:
test = """abcdefgh\nghijklmn"""
expectd_test_result = """abcdffaa\nghjaabcc"""

### input file path
task = "hepxcrrq"

### functions
def has_straight(passwd):
    i = 0
    for i in range(len(passwd) - 2):
        if ord(passwd[i]) == (ord(passwd[i+1]) - 1) and ord(passwd[i]) == (ord(passwd[i+2]) - 2):
            return True
    return False

def has_no_forbidden(passwd):
    forbidden = ['i', 'o', 'l']
    for forb in forbidden:
        if forb in passwd:
            return False
    return True

def has_two_pairs(passwd):
    for i in range(len(passwd) - 1):
        if passwd[i] == passwd[i+1]:
            for j in range(i+2, len(passwd) - 1):
                if passwd[j] == passwd[j+1]:
                    return True
    return False

def check_passwd(passwd):
    return has_straight(passwd) and has_no_forbidden(passwd) and has_two_pairs(passwd)

# ord('a') = 97 | ord('z') = 122
def increment_passwd(passwd):
    new_letter_ord = ord(passwd[-1]) + 1
    if new_letter_ord == 123:
        new_passwd = passwd[:-1]
        return increment_passwd(new_passwd) + 'a'
    else:
        passwd = passwd[:-1] + chr(new_letter_ord)
        return passwd
    
def gen_next_passwd(passwd):
    while True:
        next_candidate = increment_passwd(passwd)
        if check_passwd(next_candidate):
            break
        else:
            passwd = next_candidate
    return next_candidate

### main 
# mode = "TEST"
mode = "TASK"

print("\nMode: " + mode)
if mode == "TASK":
    input = task
    next_passwd = gen_next_passwd(input)
    print("Santa next password: " + next_passwd)
    next_passwd = gen_next_passwd(next_passwd)
    print("And next Santa password: " + next_passwd)
elif mode == "TEST":
    input = test
    test_result = []
    for test_p in input.splitlines():
        test_result.append(gen_next_passwd(test_p))
    print("Expected: " + expectd_test_result.splitlines()[0] + " | Test: " + test_result[0])
    print("Expected: " + expectd_test_result.splitlines()[1] + " | Test: " + test_result[1])