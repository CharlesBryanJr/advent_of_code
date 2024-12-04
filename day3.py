'''
--- Day 3: Mull It Over ---
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
'''

import re

def extract_numbers(regex, s):
    matches = regex.finditer(s)
    results = []
    for match in matches:
        results.append((int(match.group(1)), int(match.group(2))))
    return results

def process_word(word):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    regex = re.compile(pattern)
    numbers = extract_numbers(regex, word)
    if numbers:
        print(f"Valid mul expression(s) found in: {word}")
        for num_pair in numbers:
            print(f"Numbers: {num_pair}")
        return True
    return False


'''
if __name__ == "__main__":
    window_size = 15  # Adjust this value as needed
    with open('day3_input.txt', 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                print(f'Processing word: {word}')
                for i in range(len(word) - window_size + 1):
                    window = word[i:i+window_size]
                    if process_window(window):
                        break  # Move to next word if a valid expression is found
                print()
            break  # Remove this if you want to process all lines
'''


if __name__ == "__main__":
    words = ["<#mul(645,89)", "mul(645,89)", "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
    for word in words:
        print(f'Processing word: {word}')
        if not process_word(word):
            print("No valid mul expressions found in this word.")
        print()
