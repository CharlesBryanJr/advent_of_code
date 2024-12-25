# pylint: disable=all
'''
--- Day 6: Guard Gallivant ---
The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
'''

def get_position_of_char(arr, char):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == char:
                return (i, j)
    print(f'DID NOT FOUND CHAR: {char}')
    return None


def get_boundaries(arr):
    rows = len(arr)
    cols = len(arr[0]) if len(arr) > 0 else 0
    start_row, start_col = 0, 0
    end_row, end_col= rows - 1, cols - 1
    boundaries = {
        'start_row': start_row,
        'start_col': start_col,
        'end_row': end_row,
        'end_col': end_col
    }
    return boundaries


def traverse_map(arr, position, boundaries, direction):
    row_position, col_position  = position[0], position[1]
    valid_positions = ['.', 'X', '^']
    if arr[row_position][col_position] in valid_positions:
        arr[row_position][col_position] = 'X'
    else:
        print(f"INVALID POSITION at ({row_position}, {col_position})! Value: {arr[row_position][col_position]}")

    LAST_VISITED_POSITION = None
    if direction.lower() == 'up':
        for i in reversed(range(row_position)):
            if arr[i][col_position] not in valid_positions:
                print(f'FOUND obstruction at {i, col_position} - turn right 90 degrees!')
                LAST_VISITED_POSITION = (i + 1, col_position)
                print(f'LAST_VISITED_POSITION: {LAST_VISITED_POSITION}')
                return LAST_VISITED_POSITION
            else:
                arr[i][col_position] = 'X'
    elif direction.lower() == 'down':
        for i in range(row_position + 1, boundaries['end_row'] + 1):
            print(arr[i][col_position])
            if arr[i][col_position] not in valid_positions:
                print(f'FOUND obstruction at {i, col_position} - turn right 90 degrees!')
                LAST_VISITED_POSITION = (i - 1, col_position)
                print(f'LAST_VISITED_POSITION: {LAST_VISITED_POSITION}')
                return LAST_VISITED_POSITION
            else:
                arr[i][col_position] = 'X'
    elif direction.lower() == 'right':
        for i in range(col_position + 1, boundaries['end_col'] + 1):
            print(arr[row_position][i])
            if arr[row_position][i] not in valid_positions:
                print(f'FOUND obstruction at {row_position, i} - turn right 90 degrees!')
                LAST_VISITED_POSITION = (row_position, i - 1)
                print(f'LAST_VISITED_POSITION: {LAST_VISITED_POSITION}')
                return LAST_VISITED_POSITION
            else:
                arr[row_position][i] = 'X'
    elif direction.lower() == 'left':
        for i in reversed(range(col_position)):
            if arr[row_position][i] not in valid_positions:
                print(f'FOUND obstruction at {row_position, i} - turn right 90 degrees!')
                LAST_VISITED_POSITION = (row_position, i + 1)
                print(f'LAST_VISITED_POSITION: {LAST_VISITED_POSITION}')
                return LAST_VISITED_POSITION
            else:
                arr[row_position][i] = 'X'
    else:
        print(f'INVALID DIRECTION: {direction}')

    print(f'NO obstruction FOUND')
    return LAST_VISITED_POSITION


def get_new_direction(previous_direction):
    direction_map = {
        'up': 'right',
        'right': 'down',
        'down': 'left',
        'left': 'up'
    }
    return direction_map.get(previous_direction)


def get_new_position(position, new_direction):
    row, col = position
    new_position = None

    if new_direction == 'up':
        new_position = (row - 1, col)
    elif new_direction == 'down':
        new_position = (row + 1, col)
    elif new_direction == 'right':
        new_position = (row, col + 1)
    elif new_direction == 'left':
        new_position = (row, col - 1)
    else:
        print(f"Invalid direction: {new_direction}")

    return new_position


def count_char_in_grid(grid, char):
    char_count = 0
    for row in grid:
        char_count += row.count(char)
    return char_count


if __name__ == "__main__":
    with open('day6_input.txt', 'r') as file:
        arr = []
        for line in file:
            new_row = []
            words = line.split()
            for word in words:
                for char in word:
                    new_row.append(char)
            arr.append(new_row)

    char = '^'
    position_of_char = get_position_of_char(arr, char)
    print(f'position_of_char - {position_of_char}')
    boundaries = get_boundaries(arr)
    print(f'boundaries - {boundaries}')
    direction = 'up'
    LAST_VISITED_POSITION = True
    while LAST_VISITED_POSITION is not None:
        # Attempt to traverse the map in the current direction
        LAST_VISITED_POSITION = traverse_map(arr, position_of_char, boundaries, direction)
        if LAST_VISITED_POSITION:
            print(f'LAST_VISITED_POSITION: {LAST_VISITED_POSITION}')
            
            # Turn right and get the new direction
            direction = get_new_direction(direction)
            print(f'new_direction: {direction}')
            
            # Update the guard's position based on the new direction
            position_of_char = get_new_position(LAST_VISITED_POSITION, direction)
            print(f'new_position: {position_of_char}')
            
            # Print the current state of the map
            for row in arr:
                print(''.join(row))
        else:
            # If no obstruction is found, the guard has left the mapped area
            print(f'NO obstruction FOUND - {LAST_VISITED_POSITION}')
            print(f'guard left the mapped area')
            break
    
    char = 'X'
    print(f'Char Count {char}: {count_char_in_grid(arr, char)}')
    

