# pylint: disable=all
'''
--- Day 5: Print Queue ---
Satisfied with their search on Ceres, the squadron of scholars suggests subsequently scanning the stationery stacks of sub-basement 17.

The North Pole printing department is busier than ever this close to Christmas, and while The Historians continue their search of this historically significant facility, an Elf operating a very familiar printer beckons you over.

The Elf must recognize you, because they waste no time explaining that the new sleigh launch safety manual updates won't print correctly. Failure to update the safety manuals would be dire indeed, so you offer your services.

Safety protocols clearly indicate that new pages for the safety manuals must be printed in a very specific order. The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, page number X must be printed at some point before page number Y.

The Elf has for you both the page ordering rules and the pages to produce in each update (your puzzle input), but can't figure out whether each update has the pages in the right order.

For example:

47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
The first section specifies the page ordering rules, one per line. The first rule, 47|53, means that if an update includes both page number 47 and page number 53, then page number 47 must be printed at some point before page number 53. (47 doesn't necessarily need to be immediately before 53; other pages are allowed to be between them.)

The second section specifies the page numbers of each update. Because most safety manuals are different, the pages needed in the updates are different too. The first update, 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.

To get the printers going as soon as possible, start by identifying which updates are already in the right order.

In the above example, the first update (75,47,61,53,29) is in the right order:

75 is correctly first because there are rules that put each other page after it: 75|47, 75|61, 75|53, and 75|29.
47 is correctly second because 75 must be before it (75|47) and every other page must be after it according to 47|61, 47|53, and 47|29.
61 is correctly in the middle because 75 and 47 are before it (75|61 and 47|61) and 53 and 29 are after it (61|53 and 61|29).
53 is correctly fourth because it is before page number 29 (53|29).
29 is the only page left and so is correctly last.
Because the first update does not include some page numbers, the ordering rules involving those missing page numbers are ignored.

The second and third updates are also in the correct order according to the rules. Like the first update, they also do not include every page number, and so only some of the ordering rules apply - within each update, the ordering rules that involve missing page numbers are not used.

The fourth update, 75,97,47,61,53, is not in the correct order: it would print 75 before 97, which violates the rule 97|75.

The fifth update, 61,13,29, is also not in the correct order, since it breaks the rule 29|13.

The last update, 97,13,75,29,47, is not in the correct order due to breaking several rules.

For some reason, the Elves also need to know the middle page number of each update being printed. Because you are currently only printing the correctly-ordered updates, you will need to find the middle page number of each correctly-ordered update. In the above example, the correctly-ordered updates are:

75,47,61,53,29
97,61,53,29,13
75,29,13
These have middle page numbers of 61, 53, and 29 respectively. Adding these page numbers together gives 143.

Of course, you'll need to be careful: the actual list of page ordering rules is bigger and more complicated than the above example.

Determine which updates are already in the correct order. What do you get if you add up the middle page number from those correctly-ordered updates?
'''

import re

def extract_and_convert_page_ordering_rule(value):
    # Regex to match two numbers separated by '|'
    match = re.match(r'(\d+)\|(\d+)', value)
    if match:
        # Convert both matched numbers to integers and return them as a tuple
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        return num1, num2
    else:
        return None  # Return None if the format is not matched


def extract_and_convert_pages_to_produce(value):
    # Regex to match one or more sets of comma-separated numbers
    match = re.findall(r'\d+(?:,\d+)*', value)
    
    # If matches are found, process them
    if match:
        result = []
        for m in match:
            # Split the matched string into integers and add as a list
            nums = list(map(int, m.split(',')))
        return nums
    else:
        print("return None  # Return None if no match is found")
        return None
    

def find_middle_page_numbers(middle_page_number_array):
    middle_pages = []
    for pages in middle_page_number_array:
        middle_index = len(pages) // 2  # Find the middle index
        middle_pages.append(pages[middle_index])  # Get the middle page
    return middle_pages


def move_element(arr, from_index, to_index):
    result = arr.copy()
    element = result[from_index]
    result.pop(from_index)
    result.insert(to_index, element)
    return result


def difference_between_arrays(array1, array2):
    # Convert inner lists to tuples for set operations
    set1 = set(tuple(lst) for lst in array1)
    set2 = set(tuple(lst) for lst in array2)
    
    # Find the difference
    diff = set2 - set1
    
    # Convert tuples back to lists
    return [list(t) for t in diff]


if __name__ == "__main__":
    with open('day5_input.txt', 'r') as file:
        pages_to_produce_in_each_update = False
        pages_to_produce_array = []
        page_ordering_rules = {}
        for line in file:
            words = line.split()
            if words == []:
                pages_to_produce_in_each_update = True
            
            for word in words:
                if pages_to_produce_in_each_update == True:
                    pages_to_produce = extract_and_convert_pages_to_produce(word)
                    pages_to_produce_array.append(pages_to_produce)
                else:
                    page_ordering_rule = extract_and_convert_page_ordering_rule(word)
                    if page_ordering_rule:
                        if page_ordering_rule[0] in page_ordering_rules:
                            page_ordering_rules[page_ordering_rule[0]].add(page_ordering_rule[1])
                        else:
                            page_ordering_rules[page_ordering_rule[0]] = {page_ordering_rule[1]}

    
    print('-'*13)
    print('-'*13)
    print('-'*13)
    correctly_ordered_originally_middle_page_number_array = []
    for pages_to_produce in pages_to_produce_array:
        if pages_to_produce is not None:
            correctly_ordered = True
            for i in range(len(pages_to_produce)):
                if pages_to_produce[i] in page_ordering_rules:
                    j = i - 1
                    lowest_index_to_swap_with = None
                    while j >= 0:
                        if pages_to_produce[j] in page_ordering_rules[pages_to_produce[i]]:
                            print(pages_to_produce)
                            print(f'{pages_to_produce[i]} - {page_ordering_rules[pages_to_produce[i]]}')
                            print(f'found {pages_to_produce[j]} in set')
                            correctly_ordered = False
                            print()
                        j -= 1
            if correctly_ordered:
                correctly_ordered_originally_middle_page_number_array.append(pages_to_produce)                
        else:
            print("pages_to_produce is None")
    
    print(f'correctly_ordered_originally_middle_page_number_array - {correctly_ordered_originally_middle_page_number_array}')
    correctly_ordered_originally_middle_pages = find_middle_page_numbers(correctly_ordered_originally_middle_page_number_array)
    print(f'correctly_ordered_originally_middle_pages - {correctly_ordered_originally_middle_pages}')
    print(f'correctly_ordered_originally_middle_pages_sum = {sum(correctly_ordered_originally_middle_pages)}')


    incorrectly_ordered_originally_middle_page_number_array = []
    for pages_to_produce in pages_to_produce_array:
        if pages_to_produce is not None:
            i = 0
            while i < len(pages_to_produce):
                current_page = pages_to_produce[i]
                correctly_ordered_originally = None
                lowest_index_to_swap_with = None
                if current_page in page_ordering_rules:
                    j = i - 1
                    while j >= 0:
                        if pages_to_produce[j] in page_ordering_rules[current_page]:
                            print(pages_to_produce)
                            print(f'{current_page} - {page_ordering_rules[current_page]}')
                            print(f'found {pages_to_produce[j]} in set')
                            lowest_index_to_swap_with = j
                            print(f'lowest_index_to_swap_with: {lowest_index_to_swap_with}')
                            print()
                        j -= 1

                    if lowest_index_to_swap_with is not None:
                        pages_to_produce = move_element(pages_to_produce, i, lowest_index_to_swap_with)
                        print(f'updated_pages_to_produce - {pages_to_produce}')
                        correctly_ordered_originally = False
                    else:
                        i += 1
                else:
                    i += 1

            print('***')
            if not correctly_ordered_originally:
                print(f'updated_pages_to_produce - {pages_to_produce}')
                incorrectly_ordered_originally_middle_page_number_array.append(pages_to_produce)
        else:
            print("pages_to_produce is None")

    
    print('---')
    print('---')
    print('---')
    print(f'correctly_ordered_originally_middle_page_number_array - {correctly_ordered_originally_middle_page_number_array}')
    correctly_ordered_originally_middle_pages = find_middle_page_numbers(correctly_ordered_originally_middle_page_number_array)
    print(f'correctly_ordered_originally_middle_pages - {correctly_ordered_originally_middle_pages}')
    print(f'correctly_ordered_originally_middle_pages_sum = {sum(correctly_ordered_originally_middle_pages)}')
    print('---')
    print('---')
    print('---')
    incorrectly_ordered_originally_middle_page_number_array = difference_between_arrays(correctly_ordered_originally_middle_page_number_array, incorrectly_ordered_originally_middle_page_number_array)
    print(f'incorrectly_ordered_originally_middle_page_number_array - {incorrectly_ordered_originally_middle_page_number_array}')
    incorrectly_ordered_originally_middle_pages = find_middle_page_numbers(incorrectly_ordered_originally_middle_page_number_array)
    print(f'incorrectly_ordered_originally_middle_pages - {incorrectly_ordered_originally_middle_pages}')
    print(f'incorrectly_ordered_originally_middle_pages_sum = {sum(incorrectly_ordered_originally_middle_pages)}')    


    
    










'''
    print('-'*13)
    print('-'*13)
    print('-'*13)
    middle_page_number_array = []
    for pages_to_produce in pages_to_produce_array:
        if pages_to_produce is not None:
            correctly_ordered = True
            for i in range(len(pages_to_produce)):
                if pages_to_produce[i] in page_ordering_rules:
                    j = i - 1
                    lowest_index_to_swap_with = None
                    while j >= 0:
                        if pages_to_produce[j] in page_ordering_rules[pages_to_produce[i]]:
                            print(pages_to_produce)
                            print(f'{pages_to_produce[i]} - {page_ordering_rules[pages_to_produce[i]]}')
                            print(f'found {pages_to_produce[j]} in set')
                            lowest_index_to_swap_with = j
                            print(f'lowest_index_to_swap_with: {lowest_index_to_swap_with}')
                            correctly_ordered = False
                            print()
                        j -= 1
                    if lowest_index_to_swap_with is not None:
                        updated_pages_to_produce = move_element(pages_to_produce, i, lowest_index_to_swap_with)
                        print(f'updated_pages_to_produce - {updated_pages_to_produce}')
                    print('-')
            if correctly_ordered:
                middle_page_number_array.append(pages_to_produce)                
        else:
            print("pages_to_produce is None")
    
    print(f'middle_page_number_array - {middle_page_number_array}')
    middle_pages = find_middle_page_numbers(middle_page_number_array)
    print(f'middle_pages - {middle_pages}')
    print(f'middle_pages_sum = {sum(middle_pages)}')
'''




