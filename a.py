def is_safe(levels):
    if len(levels) < 2:
        return True
    diff = levels[1] - levels[0]
    if abs(diff) > 3 or diff == 0:
        return False
    increasing = diff > 0
    for i in range(2, len(levels)):
        new_diff = levels[i] - levels[i-1]
        if (increasing and new_diff <= 0) or (not increasing and new_diff >= 0):
            return False
        if abs(new_diff) > 3 or new_diff == 0:
            return False
    return True

def is_safe_with_dampener(levels):
    if is_safe(levels):
        return True
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe(new_levels):
            return True
    return False

safe_count = 0
with open('day2_input.txt', 'r') as file:
    for line in file:
        levels = list(map(int, line.strip().split()))
        if is_safe_with_dampener(levels):
            safe_count += 1

print(f"Number of safe reports: {safe_count}")