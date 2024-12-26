# pylint: disable=all
'''
--- Day 9: Disk Fragmenter ---
Another push of the button leaves you in the familiar hallways of some friendly amphipods! Good thing you each somehow got your own personal mini submarine. The Historians jet away in search of the Chief, mostly by driving directly into walls.

While The Historians quickly figure out how to pilot these things, you notice an amphipod in the corner struggling with his computer. He's trying to make more contiguous free space by compacting all of the files, but his program isn't working; you offer to help.

He shows you the disk map (your puzzle input) he's already generated. For example:

2333133121414131402
The disk map uses a dense format to represent the layout of files and free space on the disk. The digits alternate between indicating the length of a file and the length of free space.

So, a disk map like 12345 would represent a one-block file, two blocks of free space, a three-block file, four blocks of free space, and then a five-block file. A disk map like 90909 would represent three nine-block files in a row (with no free space between them).

Each file on disk also has an ID number based on the order of the files as they appear before they are rearranged, starting with ID 0. So, the disk map 12345 has three files: a one-block file with ID 0, a three-block file with ID 1, and a five-block file with ID 2. Using one character for each block where digits are the file ID and . is free space, the disk map 12345 represents these individual blocks:

0..111....22222
The first example above, 2333133121414131402, represents these individual blocks:

00...111...2...333.44.5555.6666.777.888899
The amphipod would like to move file blocks one at a time from the end of the disk to the leftmost free space block (until there are no gaps remaining between file blocks). For the disk map 12345, the process looks like this:

0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......
The first example requires a few more steps:

00...111...2...333.44.5555.6666.777.888899
009..111...2...333.44.5555.6666.777.88889.
0099.111...2...333.44.5555.6666.777.8888..
00998111...2...333.44.5555.6666.777.888...
009981118..2...333.44.5555.6666.777.88....
0099811188.2...333.44.5555.6666.777.8.....
009981118882...333.44.5555.6666.777.......
0099811188827..333.44.5555.6666.77........
00998111888277.333.44.5555.6666.7.........
009981118882777333.44.5555.6666...........
009981118882777333644.5555.666............
00998111888277733364465555.66.............
0099811188827773336446555566..............
The final step of this file-compacting process is to update the filesystem checksum. To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in position 0. If a block contains free space, skip it instead.

Continuing the first example, the first few blocks' position multiplied by its file ID number are 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32, and so on. In this example, the checksum is the sum of these, 1928.

Compact the amphipod's hard drive using the process he requested. What is the resulting filesystem checksum? (Be careful copy/pasting the input for this puzzle; it is a single, very long line.)
'''


# 2333133121414131402
# [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]
# 00...111...2...333.44.5555.6666.777.888899
# 0099811188827773336446555566..............


def get_disk_map_expanded_format(disk_map_dense_format):
    disk_map_expanded_format = []
    is_file_length = True
    file_id_number = 0
    
    for i in range(len(disk_map_dense_format)):
        if is_file_length:
            file_length = int(disk_map_dense_format[i])  # Convert to integer
            # Add file_id_number file_length times
            disk_map_expanded_format.extend([file_id_number] * file_length)
            #print(f'file_id_number: {file_id_number}')
            #print(f'file_length: {file_length}')
            file_id_number += 1
            is_file_length = False
        else:
            free_space_length = int(disk_map_dense_format[i])  # Convert to integer
            #print(f'free_space_length: {free_space_length}')
            # Add '.' free_space_length times
            disk_map_expanded_format.extend(['.'] * free_space_length)
            is_file_length = True
        #print(f'disk_map_expanded_format: {disk_map_expanded_format}')
        #print()
        
    return disk_map_expanded_format


def move_char_to_end_array(disk_map_expanded_format, char):
    rearranged_disk_map_expanded_format = disk_map_expanded_format.copy()
    l = 0
    r = len(rearranged_disk_map_expanded_format) - 1
    while l < r:
        while rearranged_disk_map_expanded_format[l] != char:
            l += 1
        #print(f'l: {l}')
        #print(f'{rearranged_disk_map_expanded_format[l]}')

        while rearranged_disk_map_expanded_format[r] == char:
            r -= 1
        #print(f'r: {r}')
        #print(f'{rearranged_disk_map_expanded_format[r]}')

        rearranged_disk_map_expanded_format[l], rearranged_disk_map_expanded_format[r] = rearranged_disk_map_expanded_format[r], rearranged_disk_map_expanded_format[l]
        l += 1
        r -= 1

    return rearranged_disk_map_expanded_format


def calculate_filesystem_checksum(rearranged_disk_map_expanded_format):
    filesystem_checksum = 0
    for i in range(len(rearranged_disk_map_expanded_format)):
        if not isinstance(rearranged_disk_map_expanded_format[i], int):
            return filesystem_checksum
        PRODUCT = i * rearranged_disk_map_expanded_format[i]
        filesystem_checksum += PRODUCT
        #print(f'PRODUCT: {PRODUCT}')
        #print(f'filesystem_checksum: {filesystem_checksum}')
    return filesystem_checksum


if __name__ == "__main__":
    disk_map_dense_format = []
    with open('day9_input.txt', 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                for char in word:
                    disk_map_dense_format.append(int(char))
    print('-'*13)
    print('-'*13)
    print('-'*13)
    print(f'disk_map_dense_format: {disk_map_dense_format}')
    disk_map_expanded_format = get_disk_map_expanded_format(disk_map_dense_format)
    print(f'disk_map_expanded_format: {disk_map_expanded_format}')
    char = '.' 
    rearranged_disk_map_expanded_format = move_char_to_end_array(disk_map_expanded_format, char)
    print(f'rearranged_disk_map_expanded_format: {rearranged_disk_map_expanded_format}')
    rearranged_disk_map_expanded_format_str = ''.join(str(x) for x in rearranged_disk_map_expanded_format if isinstance(x, (int, str)))
    print(f'rearranged_disk_map_expanded_format_str: {rearranged_disk_map_expanded_format_str}')
    filesystem_checksum = calculate_filesystem_checksum(rearranged_disk_map_expanded_format)
    print(f'filesystem_checksum: {filesystem_checksum}')