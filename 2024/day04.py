import sys
import re

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day4_input.txt"

### Start of test case ###
test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

test_XMAS = 18
#test_mul2 = 48
### End of test case ###

matrix = []

def input_to_2d_array(string):
    result = []
    for line in input.splitlines():
        larray = []
        for char in line:
            larray.append(char)
        result.append(larray)
    global matrix
    matrix = result

def find_xmas():
    result = 0
    global matrix
    width = len(matrix[1])
    height = len(matrix)
    print("Array size: " + str(width) + "x" + str(height))
    y_cord = 0
    for line in matrix:
        x_cord = 0
        for char in line:
            if char == 'X':
                result = result + check_xmas_with_pos(x_cord, y_cord)
            x_cord = x_cord+1
        y_cord = y_cord +1
    return result


def check_dir_xmas(x, y, ang):
    buffor = ''
    global matrix
    if ang == 0:
        buffor = str(matrix[y][x]) + str(matrix[y][x+1]) + str(matrix[y][x+2]) + str(matrix[y][x+3])
    elif ang == 45:
        buffor = str(matrix[y][x]) + str(matrix[y-1][x+1]) + str(matrix[y-2][x+2]) + str(matrix[y-3][x+3])
    elif ang == 90:
        buffor = str(matrix[y][x]) + str(matrix[y-1][x]) + str(matrix[y-2][x]) + str(matrix[y-3][x])
    elif ang == 135:
        buffor = str(matrix[y][x]) + str(matrix[y - 1][x-1]) + str(matrix[y - 2][x-2]) + str(matrix[y - 3][x-3])
    elif ang == 180:
        buffor = str(matrix[y][x]) + str(matrix[y][x-1]) + str(matrix[y][x-2]) + str(matrix[y][x-3])
    elif ang == 225:
        buffor = str(matrix[y][x]) + str(matrix[y + 1][x-1]) + str(matrix[y + 2][x-2]) + str(matrix[y + 3][x-3])
    elif ang == 270:
        buffor = str(matrix[y][x]) + str(matrix[y + 1][x]) + str(matrix[y + 2][x]) + str(matrix[y + 3][x])
    elif ang == 315:
        buffor = str(matrix[y][x]) + str(matrix[y + 1][x + 1]) + str(matrix[y + 2][x +2]) + str(matrix[y + 3][x +3])
    return buffor == 'XMAS'

def check_xmas_with_pos(x, y):
    result = 0
    if x <= (len(matrix[1]) - 4):
        if check_dir_xmas(x, y, 0):
            result = result + 1
    if x <= (len(matrix[1]) - 4) and y >= 3:
        if check_dir_xmas(x, y, 45):
            result = result + 1
    if y >= 3:
        if check_dir_xmas(x, y, 90):
            result = result + 1
    if x >= 3 and y >= 3:
        if check_dir_xmas(x, y, 135):
            result = result + 1
    if x >= 3:
        if check_dir_xmas(x, y, 180):
            result = result + 1
    if x >= 3 and y <= (len(matrix) -4):
        if check_dir_xmas(x, y, 225):
            result = result + 1
    if y <= (len(matrix) -4):
        if check_dir_xmas(x, y, 270):
            result = result + 1
    if x <= (len(matrix[1]) -4)  and y <= (len(matrix) -4):
        if check_dir_xmas(x, y, 315):
            result = result + 1
    return result

def find_x_mas():
    result = 0
    global matrix
    width = len(matrix[1])
    height = len(matrix)
    print("Array size: " + str(width) + "x" + str(height))
    for y in range(1, len(matrix)-1):
        for x in range(1, len(matrix[1])-1):
            if matrix[y][x] == 'A':
                result = result + check_x_mas(x, y)
    return result

def check_x_mas(x, y):
    charTL = matrix[y-1][x-1]
    charTR = matrix[y-1][x+1]
    charBL = matrix[y+1][x-1]
    charBR = matrix[y+1][x+1]

    mas1 = (charTL=='M' and charBR == 'S') or (charTL=='S' and charBR == 'M')
    mas2 = (charTR=='M' and charBL=='S') or (charTR=='S' and charBL=='M')
    return mas1 and mas2

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

input_to_2d_array(input)
buffor = find_x_mas()
print(buffor)


#if mode == "TEST":
#    print("test status: " + str(res == test_mul2))
