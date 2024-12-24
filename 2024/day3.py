# pylint: disable=all

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

Your puzzle answer was 179571322.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
'''

import re

def extract_numbers(regex, s):
    matches = regex.finditer(s)
    results = []
    for match in matches:
        results.append((int(match.group(1)), int(match.group(2))))
    return results


def get_mul_pattern_dictionary(regex, s):
    matches = regex.finditer(s)
    results = []
    match_count = 0
    for match in matches:
        match_count += 1
        match_details = {
            f"Match {match_count} details": {
                "Full match": match.group(),
                "Start position": str(match.start()),
                "End position": str(match.end()),
                "Extracted numbers": f"{match.group(1)}, {match.group(2)}",
                "Multiplication result": f"{int(match.group(1))*int(match.group(2))}"
            }
        }
        
        try:
            number_pair = (int(match.group(1)), int(match.group(2)))
            results.append(match_details)
            print(f'Match {match_count} details:')
            print(f'  Full match: {match.group()}')
            print(f'  Start position: {match.start()}')
            print(f'  End position: {match.end()}')
            print(f'  Extracted numbers: {match.group(1)}, {match.group(2)}')
            print(f'  Multiplication result: {number_pair[0]} × {number_pair[1]} = {number_pair[0] * number_pair[1]}')
        
        except (ValueError, IndexError) as e:
            print(f'  Error processing match: {e}')
    
    print(f'\nTotal matches found: {match_count}')
    print(f'results: {results}')
    return results

def get_string_pattern_dictionary(regex, s):
    matches = regex.finditer(s)
    results = []
    match_count = 0
    for match in matches:
        match_count += 1
        match_details = {
            f"Match {match_count} details": {
                "Full match": match.group(),
                "Start position": str(match.start()),
                "End position": str(match.end())
            }
        }
        
        try:
            results.append(match_details)
            print(f'Match {match_count} details:')
            print(f'  Full match: {match.group()}')
            print(f'  Start position: {match.start()}')
            print(f'  End position: {match.end()}')
        
        except (ValueError, IndexError) as e:
            print(f'  Error processing match: {e}')
    
    print(f'Total matches found: {match_count}')
    print(f'results: {results}')
    return results

def process_word(word, is_part_1 = True):
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    mul_regex = re.compile(mul_pattern)
    mul_pattern_dictionary = get_mul_pattern_dictionary(mul_regex, word)
    print()
    dont_string_pattern = r"don't()"
    dont_string_pattern_regex = re.compile(dont_string_pattern)
    dont_pattern_dictionary = get_string_pattern_dictionary(dont_string_pattern_regex, word)
    print()
    do_string_pattern = r"do()"
    do_string_pattern_regex = re.compile(do_string_pattern)
    do_pattern_dictionary = get_string_pattern_dictionary(do_string_pattern_regex, word)
    print()
    enable_mul = True
    #if mul_pattern_dictionary:
        #print(f'process_mul_instructions: {process_mul_instructions(mul_pattern_dictionary, dont_pattern_dictionary, do_pattern_dictionary)}')
    return mul_pattern_dictionary, dont_pattern_dictionary, do_pattern_dictionary

def sum_multiplication_results(results):
    total = 0
    for match in results:
        match_key = list(match.keys())[0]
        multiplication_result = int(match[match_key]['Multiplication result'])
        total += multiplication_result
    return total

def sum_enabled_mul_instructions(full_mul_pattern_dictionary, disabled_intervals):
    return True


def find_intervals(dont_dict, do_dict):
    intervals = []
    
    dont_ends = []
    for sublist in dont_dict:
        for match in sublist:
            for key, value in match.items():
                if 'Match' in key and 'details' in key:
                    dont_ends.append(int(value['End position']))
    
    do_starts = []
    for sublist in do_dict:
        for match in sublist:
            for key, value in match.items():
                if 'Match' in key and 'details' in key:
                    do_starts.append(int(value['Start position']))
    
    dont_ends.sort()
    do_starts.sort()
    
    for end in dont_ends:
        for start in do_starts:
            if start > end:
                intervals.append([end, start])
                break
    
    return intervals


if __name__ == "__main__":
    total = 0
    is_part_1 = False
    full_mul_pattern_dictionary = []
    full_dont_pattern_dictionary = []
    full_do_pattern_dictionary = []
    with open('day3_input.txt', 'r') as file:
        for line in file:
            words = line.split()
            #words = ["<#mul(645,89)", "mul(645,89)", "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
            #words = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
            #words = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
            for word in words:
                print()
                print(f'Processing word: {word}')
                mul_pattern_dictionary, dont_pattern_dictionary, do_pattern_dictionary = process_word(word, is_part_1)
                full_mul_pattern_dictionary.append(mul_pattern_dictionary)
                res = sum_multiplication_results(mul_pattern_dictionary)
                full_dont_pattern_dictionary.append(dont_pattern_dictionary)
                full_do_pattern_dictionary.append(do_pattern_dictionary)
                if res > 1:
                    print(f'total: {total}')
                    print(f'res: {res}')
                    total += res
                    print(f'new total: {total}')
                print()
                print()
                print()
                print(f'full_mul_pattern_dictionary: {full_mul_pattern_dictionary}')
                print()
                print()
                print()
                print(f'full_dont_pattern_dictionary: {full_dont_pattern_dictionary}')
                print()
                print()
                print()
                print(f'full_do_pattern_dictionary: {full_do_pattern_dictionary}')
                print()
                print()
                print()
                print(f'find_intervals: {find_intervals(full_dont_pattern_dictionary, full_do_pattern_dictionary)}')                
                break
            break

