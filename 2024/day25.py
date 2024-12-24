# pylint: disable=all

'''
'''

            
if __name__ == "__main__":
    left, right = [], []
    with open('day25_input.txt', 'r') as file:
        for line in file:
            words = line.split()
            print(words)
            for word in words:
                print(word)
            break