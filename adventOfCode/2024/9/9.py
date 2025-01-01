import numpy as np

def parse_text(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

if __name__ == "__main__":
    # Get input
    disk_map_compressed = parse_text('9-input1.txt')
    
    # Pre-calculate total length and create array at once
    total_length = sum(int(c) for c in disk_map_compressed)
    disk_map = np.empty(total_length, dtype=np.int64)
    
    # Fill array in one pass
    pos = 0
    id = 0
    for i, v in enumerate(disk_map_compressed, start=1):
        length = int(v)
        if i % 2 == 0:
            disk_map[pos:pos+length] = -1
        else:
            disk_map[pos:pos+length] = id
            id += 1
        pos += length
    
    # Process from end to beginning
    max_id_idx = len(disk_map)
    while id >= 0:
        id -= 1
        
        # Find the block boundaries
        while disk_map[max_id_idx - 1] != id:
            max_id_idx -= 1
            
        min_id_idx = max_id_idx - 1
        while min_id_idx > 0 and disk_map[min_id_idx - 1] == id:
            min_id_idx -= 1
            
        id_size = max_id_idx - min_id_idx
        
        # Find suitable empty slot
        min_empty_slot_idx = 0
        while True:
            while disk_map[min_empty_slot_idx] != -1:
                min_empty_slot_idx += 1
                
            max_empty_slot_idx = min_empty_slot_idx + 1
            while disk_map[max_empty_slot_idx] == -1:
                max_empty_slot_idx += 1
                
            empty_slot_size = max_empty_slot_idx - min_empty_slot_idx
            
            if empty_slot_size >= id_size:
                break
            min_empty_slot_idx += empty_slot_size
            if min_empty_slot_idx >= min_id_idx:
                break
        
        # Move block if we found a suitable spot
        if min_empty_slot_idx < min_id_idx:
            disk_map[min_empty_slot_idx:min_empty_slot_idx+id_size] = id
            disk_map[min_id_idx:max_id_idx] = -1
    
    # Calculate checksum (no need to replace -1s)
    checksum = sum(i * v for i, v in enumerate(disk_map) if v != -1)
    print(f'Filesystem checksum: {checksum}')