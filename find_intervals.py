def find_intervals(dont_dict, do_dict):
    intervals = []
    
    # Extract end positions from dont_dict
    dont_ends = []
    for sublist in dont_dict:
        for match in sublist:
            for key, value in match.items():
                if 'Match' in key and 'details' in key:
                    dont_ends.append(int(value['End position']))
    
    # Extract start positions from do_dict
    do_starts = []
    for sublist in do_dict:
        for match in sublist:
            for key, value in match.items():
                if 'Match' in key and 'details' in key:
                    do_starts.append(int(value['Start position']))
    
    # Sort the positions
    dont_ends.sort()
    do_starts.sort()
    
    # Find valid intervals
    for end in dont_ends:
        for start in do_starts:
            if start > end:
                intervals.append([end, start])
                break
    
    return intervals

# Example usage
full_dont_pattern_dictionary = [[{'Match 89 details': {'Full match': "don't", 'Start position': '20', 'End position': '25'}},
                                 {'Match 2 details': {'Full match': "don't", 'Start position': '30', 'End position': '35'}}]]
full_do_pattern_dictionary = [[{'Match 1 details': {'Full match': 'do', 'Start position': '27', 'End position': '28'}}, 
                               {'Match 89 details': {'Full match': 'do', 'Start position': '40', 'End position': '42'}},
                               {'Match 3 details': {'Full match': 'do', 'Start position': '50', 'End position': '52'}}]]

result = find_intervals(full_dont_pattern_dictionary, full_do_pattern_dictionary)
print(result)