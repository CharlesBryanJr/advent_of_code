# pylint: disable=all
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

Part 1 Answer = 2483
'''

def count_occurrences(arr, word):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    word_length = len(word)
    count = 0

    # All 8 directions: up, down, left, right, and the four diagonals
    directions = [
       (-1, 0), (1, 0), (0, -1), (0, 1),
       (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    print(f"Starting to search for '{word}' in a grid of {rows}x{cols}")
   
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == word[0]:
                print()
                print(f"Found starting letter '{word[0]}' at position ({i}, {j})")
                # Check each direction from here
                for dx, dy in directions:
                    print(f"  Checking direction dx={dx}, dy={dy}")
                    found = True
                    x, y = i, j
                    for k in range(word_length):
                        # Check bounds and char match
                        if 0 <= x < rows and 0 <= y < cols:
                            print(f"    Checking character {k} ('{word[k]}') at position ({x}, {y}) -> found '{arr[x][y]}'")
                            if arr[x][y] == word[k]:
                                # Move to next character
                                x += dx
                                y += dy
                            else:
                                print(f"    Character mismatch: expected '{word[k]}', got '{arr[x][y]}'. Stopping.")
                                found = False
                                break
                        else:
                            print(f"    Out of bounds at character {k}. Stopping.")
                            found = False
                            break
                        
                    if found:
                        print(f"  Found an occurrence of '{word}' starting at ({i}, {j}) in direction dx={dx}, dy={dy}")
                        count += 1
    
    print(f"Total occurrences of '{word}': {count}")
    return count

if __name__ == "__main__":
    arr = []
    with open('day4_input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            arr.append(list(line))

    word = 'XMAS'
    occurrences = count_occurrences(arr, word)