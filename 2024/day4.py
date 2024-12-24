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
                            #print(f"    Checking character {k} ('{word[k]}') at position ({x}, {y}) -> found '{arr[x][y]}'")
                            if arr[x][y] == word[k]:
                                # Move to next character
                                x += dx
                                y += dy
                            else:
                                #print(f"    Character mismatch: expected '{word[k]}', got '{arr[x][y]}'. Stopping.")
                                found = False
                                break
                        else:
                            #print(f"    Out of bounds at character {k}. Stopping.")
                            found = False
                            break
                        
                    if found:
                        print(f"  Found an occurrence of '{word}' starting at ({i}, {j}) in direction dx={dx}, dy={dy}")
                        # Print each character's position during the match
                        for k in range(word_length):
                            char_x = i + k * dx
                            char_y = j + k * dy
                            print(f"    Character '{word[k]}' at position ({char_x}, {char_y})")
                        count += 1
    
    print(f"Total occurrences of '{word}': {count}")
    return count


def kmp_lps(pattern):
    """
    Compute the longest prefix-suffix (LPS) array for the KMP algorithm.
    lps[i] = the longest proper prefix of pattern[:i+1] which is also a suffix of pattern[:i+1].
    """
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
                # Note: We do not increment i here
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    Return a list of starting indices where pattern is found in text using KMP.
    """
    if not pattern:
        return []

    lps = kmp_lps(pattern)
    i, j = 0, 0  # i for text, j for pattern
    occurrences = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                # Found occurrence ending at i-1
                occurrences.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return occurrences

def get_rows(arr):
    """
    Return a list of (string, start_positions) for each row.
    start_positions[i] gives the (row, col) coordinate of the i-th character in the string.
    """
    rows = []
    for r, row in enumerate(arr):
        text = ''.join(row)
        # For each character at index c in the string, the coordinate is (r, c)
        start_positions = [(r, c) for c in range(len(row))]
        rows.append((text, start_positions))
    return rows

def get_columns(arr):
    """
    Return a list of (string, start_positions) for each column.
    start_positions[i] = (row, col) of the i-th character in that column.
    """
    if not arr:
        return []
    R, C = len(arr), len(arr[0])
    cols = []
    for c in range(C):
        col_chars = [arr[r][c] for r in range(R)]
        text = ''.join(col_chars)
        start_positions = [(r, c) for r in range(R)]
        cols.append((text, start_positions))
    return cols

def get_diagonals(arr):
    """
    Extract diagonals in two directions:
    - Top-left to bottom-right (↘)
    - Top-right to bottom-left (↙)
    
    Each diagonal is represented as (text, start_positions).
    start_positions[i] gives the (row, col) for the i-th char in the diagonal.
    """
    if not arr:
        return []
    R, C = len(arr), len(arr[0])
    diagonals = []
    
    # Top-left to bottom-right (↘)
    # Diagonals start from first row and first column
    for start_col in range(C):
        text = []
        coords = []
        r, c = 0, start_col
        while r < R and c < C:
            text.append(arr[r][c])
            coords.append((r, c))
            r += 1
            c += 1
        diagonals.append((''.join(text), coords))
    # Diagonals starting from first column except the top-left corner (already included)
    for start_row in range(1, R):
        text = []
        coords = []
        r, c = start_row, 0
        while r < R and c < C:
            text.append(arr[r][c])
            coords.append((r, c))
            r += 1
            c += 1
        diagonals.append((''.join(text), coords))
    
    # Top-right to bottom-left (↙)
    # Diagonals start from first row and last column
    for start_col in range(C):
        text = []
        coords = []
        r, c = 0, start_col
        while r < R and c >= 0:
            text.append(arr[r][c])
            coords.append((r, c))
            r += 1
            c -= 1
        diagonals.append((''.join(text), coords))
    # Diagonals starting from first column at rows > 0
    for start_row in range(1, R):
        text = []
        coords = []
        r, c = start_row, C - 1
        while r < R and c >= 0:
            text.append(arr[r][c])
            coords.append((r, c))
            r += 1
            c -= 1
        diagonals.append((''.join(text), coords))
    
    return diagonals


def search_word_in_grid(arr, word):
    occurrences = []
    rev_word = word[::-1]

    # Search in rows
    for text, coords in get_rows(arr):
        # Forward occurrences
        for start_idx in kmp_search(text, word):
            found_positions = coords[start_idx:start_idx+len(word)]
            occurrences.append(found_positions)
        # Backward occurrences
        for start_idx in kmp_search(text, rev_word):
            found_positions = coords[start_idx:start_idx+len(word)]
            # These positions represent the reversed word, so they occur in reverse order.
            # If needed, reorder found_positions so that they reflect the word in the correct direction.
            # Usually not required for counting occurrences, but for clarity:
            # occurrences.append(found_positions[::-1])
            occurrences.append(found_positions[::-1])

    # Search in columns
    for text, coords in get_columns(arr):
        # Forward
        for start_idx in kmp_search(text, word):
            found_positions = coords[start_idx:start_idx+len(word)]
            occurrences.append(found_positions)
        # Backward
        for start_idx in kmp_search(text, rev_word):
            found_positions = coords[start_idx:start_idx+len(word)]
            occurrences.append(found_positions[::-1])

    # Search in diagonals
    for text, coords in get_diagonals(arr):
        # Forward
        for start_idx in kmp_search(text, word):
            found_positions = coords[start_idx:start_idx+len(word)]
            occurrences.append(found_positions)
        # Backward
        for start_idx in kmp_search(text, rev_word):
            found_positions = coords[start_idx:start_idx+len(word)]
            occurrences.append(found_positions[::-1])

    return occurrences


def count_x_mas_occurrences(grid):
    R = len(grid)
    if R == 0:
        return 0
    C = len(grid[0])
    count = 0

    # Valid patterns for each diagonal
    valid_patterns = {"MAS", "SAM"}

    for r in range(R - 2):
        for c in range(C - 2):
            # Extract diagonals
            d1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
            d2 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]

            # Check if both diagonals form "MAS" or "SAM"
            if d1 in valid_patterns and d2 in valid_patterns:
                count += 1

    return count


if __name__ == "__main__":
    arr = []
    with open('day4_input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            arr.append(list(line))

    count = 0
    word = 'XMAS'
    result = search_word_in_grid(arr, word)
    for occ in result:
        count += 1
        print("Occurrence:")
        for pos in occ:
            print(f"  {pos} -> {arr[pos[0]][pos[1]]}")
    print(f"Count: {count}")
    occurrences = count_x_mas_occurrences(arr)
    print("Number of X-MAS occurrences:", occurrences)