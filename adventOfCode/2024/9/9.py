def parse_text(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def main():
    input_text = parse_text('9-input1.txt')
    
    # Process input into disk array
    disk = []
    index = 0
    file_id = -1
    
    while index < len(input_text):
        # Process file section
        file_id += 1
        file_length = int(input_text[index])
        disk.extend([file_id] * file_length)
        index += 1
        
        if index >= len(input_text):
            break
            
        # Process blank section
        blank_length = int(input_text[index])
        disk.extend([-1] * blank_length)
        index += 1
    
    # Move files
    left_index = -1
    right_index = len(disk)
    
    while True:
        # Find next blank space from left
        while True:
            left_index += 1
            if left_index >= len(disk) or left_index >= right_index:
                return disk
            if disk[left_index] == -1:
                break
        
        # Find next file from right
        while True:
            right_index -= 1
            if right_index <= left_index:
                return disk
            if disk[right_index] != -1:
                break
        
        # Move file
        disk[left_index] = disk[right_index]
        disk[right_index] = -1
    
    return disk

if __name__ == "__main__":
    disk = main()
    # Calculate checksum
    checksum = sum(i * file_id for i, file_id in enumerate(disk) if file_id != -1)
    print(f'Filesystem checksum: {checksum}')