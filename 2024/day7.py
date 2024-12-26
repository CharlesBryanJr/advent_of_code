# pylint: disable=all

'''
--- Day 7: Bridge Repair ---
The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

For example:

190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20

Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are always evaluated left-to-right, not according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: add (+) and multiply (*).

Only three of the above equations can be made true by inserting operators:

190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.
The engineers just need the total calibration result, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is 3749.

Determine which equations could possibly be true. What is their total calibration result?
'''

import re
import itertools


def remove_non_numbers(s):
    pattern = r'[^0-9]'
    replacement = ''
    return re.sub(pattern, replacement, s)


def generate_combinations(n):
    operators = ['+', '*']
    combinations = list(itertools.product(operators, repeat=n-1))
    return combinations


def evaluate_combinations(operators_list, numbers, target):
    results = []
    found_target = False
    for operators in operators_list:
        result = numbers[0]
        for i, operator in enumerate(operators):
            if operator == '+':
                result += numbers[i + 1]  # Add the next number
            elif operator == '*':
                result *= numbers[i + 1]  # Multiply by the next number
        if result == target:
            found_target = True
        results.append(result)
    return results, found_target


def evaluate_arithmetic_equations(list_of_equations):
    total_calibration_result = 0
    for arithmetic_result, operands in list_of_equations.items():
        print(f'arithmetic_result: {arithmetic_result}')
        print(f'operands: {operands}')
        operands_combinations = generate_combinations(len(operands))
        print(f'operands_combinations: {operands_combinations}')
        evaluated_combinations, found_target = evaluate_combinations(operands_combinations, operands, arithmetic_result)
        print(f'evaluated_combinations: {evaluated_combinations}')
        print(f'found_target: {found_target}')
        if found_target:
            total_calibration_result += arithmetic_result
        print('-'*13)
        print('-'*13)
        print('-'*13)
    return total_calibration_result


if __name__ == "__main__":
    list_of_equations = {}
    with open('day7_input.txt', 'r') as file:
        for line in file:
            new_row = []
            words = line.split()
            print('-'*13)
            print('-'*13)
            print('-'*13)
            print(words)
            for word in words:
                new_row.append(int(remove_non_numbers(word)))
            
            arithmetic_result_index = 0
            arithmetic_result = new_row.pop(arithmetic_result_index)
            list_of_equations[arithmetic_result] = new_row
            print(list_of_equations)

    print('-'*13)
    print('-'*13)
    print('-'*13)
    total_calibration_result = evaluate_arithmetic_equations(list_of_equations)
    print(f'total_calibration_result: {total_calibration_result}')