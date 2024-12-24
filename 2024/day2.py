'''
--- Day 2: Red-Nosed Reports ---
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
'''


def is_increasing_by_at_least_x_and_at_most_y(arr, x=1, y=3):
    i = 1
    while i < len(arr):
        increasing_by_at_least_x = (arr[i] - arr[i - 1]) >= x
        increasing_by_at_most_y = (arr[i] - arr[i - 1]) <= y
        if not increasing_by_at_least_x or not increasing_by_at_most_y:
            return False
        i += 1
    return True


def is_decreasing_by_at_least_x_and_at_most_y(arr, x=1, y=3):
    i = 1
    while i < len(arr):
        decreasing_by_at_least_x = (arr[i - 1] - arr[i]) >= x
        decreasing_by_at_most_y = (arr[i - 1] - arr[i]) <= y
        if not decreasing_by_at_least_x or not decreasing_by_at_most_y:
            return False
        i += 1
    return True


def is_increasing_by_at_least_x_and_at_most_y_and_contains_less_than_z_errors(arr, x=1, y=3, z=1):
    errors = 0
    left, right = 0, 1
    while left <= right and right < len(arr) - 1:
        current_increment = arr[right] - arr[left]
        increasing_by_at_least_x_but_at_most_y = (current_increment >= x) and (current_increment <= y)
        if increasing_by_at_least_x_but_at_most_y:
            left += 1
        else:
            errors += 1
            if errors > z:
                return False
            right += 1
            alternative_increment = arr[right] - arr[left]
            adjacent_increasing_by_at_least_x_but_at_most_y = (alternative_increment >= x) and (alternative_increment <= y)
            if not adjacent_increasing_by_at_least_x_but_at_most_y:
                return False
    
            left = right
        right += 1    
    
    
    return True if errors <= z else False


def is_decreasing_by_at_least_x_and_at_most_y_and_contains_less_than_z_errors(arr, x=1, y=3, z=1):
    errors = 0
    left, right = 0, 1
    while left <= right and right < len(arr) - 1:
        current_increment = arr[left] - arr[right]
        decreasing_by_at_least_x_but_at_most_y = (current_increment >= x) and (current_increment <= y)
        if decreasing_by_at_least_x_but_at_most_y:
            left += 1
        else:
            errors += 1
            if errors > z:
                return False
            right += 1
            alternative_increment = arr[left] - arr[right]
            adjacent_decreasing_by_at_least_x_but_at_most_y = (alternative_increment >= x) and (alternative_increment <= y)
            if not adjacent_decreasing_by_at_least_x_but_at_most_y:
                return False
    
            left = right
        right += 1


if __name__ == "__main__":
    safe_reports_count, safe_reports_count_with_dampener = 0, 0
    a = []
    arr = []
    with open('day2_input.txt', 'r') as file:
        is_left_list = True
        for line in file:
            words = line.split()
            for word in words:
                arr.append(int(word))

            if is_increasing_by_at_least_x_and_at_most_y(arr) or is_decreasing_by_at_least_x_and_at_most_y(arr):
                safe_reports_count += 1
                safe_reports_count_with_dampener += 1
            else:
                if is_increasing_by_at_least_x_and_at_most_y_and_contains_less_than_z_errors(arr) or is_decreasing_by_at_least_x_and_at_most_y_and_contains_less_than_z_errors(arr):
                    safe_reports_count_with_dampener += 1

            arr = []

    print(f'How many reports are safe?: {safe_reports_count}')
    print(f'How many reports are safe (With Dampener): {safe_reports_count_with_dampener}')