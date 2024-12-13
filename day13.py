# pylint: disable=all

'''
--- Day 13: Claw Contraption ---
Next up: the lobby of a resort on a tropical island. The Historians take a moment to admire the hexagonal floor tiles before spreading out.

Fortunately, it looks like the resort has a new arcade! Maybe you can win some prizes from the claw machines?

The claw machines here are a little unusual. Instead of a joystick or directional buttons to control the claw, these machines have two buttons labeled A and B. Worse, you can't just put in a token and play; it costs 3 tokens to push the A button and 1 token to push the B button.

With a little experimentation, you figure out that each machine's buttons are configured to move the claw a specific amount to the right (along the X axis) and a specific amount forward (along the Y axis) each time that button is pressed.

Each machine contains one prize; to win the prize, the claw must be positioned exactly above the prize on both the X and Y axes.

You wonder: what is the smallest number of tokens you would have to spend to win as many prizes as possible? You assemble a list of every machine's button behavior and prize location (your puzzle input). For example:

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
This list describes the button configuration and prize location of four different claw machines.

For now, consider just the first claw machine in the list:

Pushing the machine's A button would move the claw 94 units along the X axis and 34 units along the Y axis.
Pushing the B button would move the claw 22 units along the X axis and 67 units along the Y axis.
The prize is located at X=8400, Y=5400; this means that from the claw's initial position, it would need to move exactly 8400 units along the X axis and exactly 5400 units along the Y axis to be perfectly aligned with the prize in this machine.
The cheapest way to win the prize is by pushing the A button 80 times and the B button 40 times. This would line up the claw along the X axis (because 80*94 + 40*22 = 8400) and along the Y axis (because 80*34 + 40*67 = 5400). Doing this would cost 80*3 tokens for the A presses and 40*1 for the B presses, a total of 280 tokens.

For the second and fourth claw machines, there is no combination of A and B presses that will ever win a prize.

For the third claw machine, the cheapest way to win the prize is by pushing the A button 38 times and the B button 86 times. Doing this would cost a total of 200 tokens.

So, the most prizes you could possibly win is two; the minimum tokens you would have to spend to win all (two) prizes is 480.

You estimate that each button would need to be pressed no more than 100 times to win a prize. How else would someone be expected to play?

Figure out how to win as many prizes as possible. What is the fewest tokens you would have to spend to win all possible prizes?
'''
import re
from math import gcd


def clean_input(data):
    pattern = r'([A-Z]):?|(\d+)'
    result = []
    
    for item in data:
        # Find all matches of letters or numbers in the item
        matches = re.findall(pattern, item)
        
        # Process each match
        filtered_matches = []
        for match in matches:
            # If either letter or number exists, add it to filtered matches
            if match[0] or match[1]:
                selected_match = match[0] if match[0] else match[1]
                filtered_matches.append(selected_match)
        
        # Extend the result list with filtered matches
        result.extend(filtered_matches)
    
    #print(result)
    return result


def group_rows(arr):
    multiple_game_input = []
    single_game_input = []
    counter = 0

    for row in arr:
        single_game_input.append(row)
        counter += 1
        if counter % 3 == 0:
            multiple_game_input.append(single_game_input)
            single_game_input = []

    # If there are any leftover rows that didn't form a complete group of 3
    if single_game_input:
        multiple_game_input.append(single_game_input)

    return multiple_game_input


def parse_game_input(game_input):
    x_units_to_move_options = []
    x_units_to_move = None
    y_units_to_move_options = []
    y_units_to_move = None
    for button in game_input:
        if button[0] == 'P':
            x_units_to_move = int(button[2])
            y_units_to_move = int(button[4])
        else:
            x_units_to_move_options.append(int(button[2]))
            y_units_to_move_options.append(int(button[4]))
    
    parsed_game_inputs = [[x_units_to_move, x_units_to_move_options], [y_units_to_move, y_units_to_move_options]]
    return parsed_game_inputs


def can_reach_target(target, options):
    if len(options) != 2:
        raise ValueError("This function expects exactly two options.")
    n1, n2 = options

    # Check gcd condition first
    g = gcd(n1, n2)
    if target % g != 0:
        return None

    # Try to find nonnegative a,b
    for a in range(target // n1 + 1):
        remainder = target - a * n1
        if remainder >= 0 and remainder % n2 == 0:
            b = remainder // n2
            # We found a combination a,b that works
            return (a, b)
    return None


def calculate_tokens(multiple_game_input, x_token_cost, y_token_cost, tokens_used):
    for game_input in multiple_game_input:
        print(f'game_input: {game_input}')
        parsed_game_inputs = parse_game_input(game_input)
        print(f'parsed_game_inputs: {parsed_game_inputs}')
        
        for parsed_game_input in parsed_game_inputs:
            print(f'parsed_game_input: {parsed_game_input}')
            target = parsed_game_input[0]
            options = [option for option in parsed_game_input[1]]
            multiples = can_reach_target(target, options)
            print(f'multiples: {multiples}')
            
            # Handle None safely
            if multiples is None:
                x_val = 0
                y_val = 0
            else:
                x_val = multiples[0] if multiples[0] is not None else 0
                y_val = multiples[1] if multiples[1] is not None else 0
            
            tokens_used += x_token_cost * x_val + y_token_cost * y_val
        
        print(f'tokens_used: {tokens_used}')
    return tokens_used


if __name__ == "__main__":
    with open('day13_input.txt', 'r') as file:
        arr = []
        for line in file:
            words = line.split()
            row = []
            for word in words:
                if word != "Button":
                    row.append(word)

            cleaned_row = clean_input(row)
            if cleaned_row != []:
                arr.append(cleaned_row)
            print('-'*13)
            print('-'*13)
            print('-'*13)
    
    x_token_cost = 3
    y_token_cost = 1
    tokens_used = 0
    multiple_game_input = group_rows(arr)
    tokens_used = calculate_tokens(multiple_game_input, x_token_cost, y_token_cost, tokens_used)
