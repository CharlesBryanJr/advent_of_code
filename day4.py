'''
--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?
'''


def get_chars_in_word(word):
    return [char for char in word]

def a(arr, chars_in_word):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            current_char = arr[i][j]
            if current_char in chars_in_word:
                print(f'Found {arr[i][j]} at location i: {i}, j: {j}')
                missing_neighbors = [char for char in chars_in_word if char != current_char]
                print(f'missing_neighbors: {missing_neighbors}')
                check_neighbors(arr, i, j, chars_in_word)
    return None

def check_neighbors(arr, i, j, missing_neighbors):
    found_neighbors = []
    neighbor_offsets = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]
    
    for dx, dy in neighbor_offsets:
        new_i, new_j = i + dx, j + dy
        if (0 <= new_i < len(arr) and 0 <= new_j < len(arr[0])):
            if arr[new_i][new_j] in missing_neighbors:
                found_neighbors.append({
                    'value': arr[new_i][new_j],
                    'location': (new_i, new_j)
                })
                print(f'Found missing neighbor {arr[new_i][new_j]} at location i: {new_i}, j: {new_j}')
    return found_neighbors

if __name__ == "__main__":
    new_row = []
    arr = []
    with open('day4_input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            #print(f'line: {line}')
            
            for char in line:
                new_row.append(char)
            #print(f'new_row: {new_row}')
            
            arr.append(new_row)
            #print(f'arr: {arr}')
            new_row = []
    
    print('-'*13)
    print('-'*13)
    print('-'*13)
    x = 0
    y = 0
    word = 'xmas'
    chars_in_word = get_chars_in_word(word.upper())
    a(arr, chars_in_word)