def find_the_total_distance(left, right):
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    total_distance = 0
    for i in range(len(left)):
        total_distance += abs(sorted_left[i] - sorted_right[i])
    return total_distance

def find_the_similarity(left, right):
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    similarity_score = 0
    for left_num in sorted_left:
        similarity_score += left_num * sorted_right.count(left_num)
    return similarity_score
            
if __name__ == "__main__":
    left, right = [], []
    with open('day1_input.txt', 'r') as file:
        is_left_list = True
        for line in file:
            words = line.split()
            for word in words:
                if is_left_list:
                    left.append(int(word.strip()))
                    is_left_list = False
                else:
                    right.append(int(word.strip()))
                    is_left_list = True
            
    print(f'the left list: {left}')
    print(f'the right list: {right}')
    print(f'the total distance between the left list and the right list: {find_the_total_distance(left, right)}')
    print(f'the similarity score between the left list and the right list: {find_the_similarity(left, right)}')

    
