def parse_input_file(filename):
    lines = []
    
    with open(filename, 'r') as file:
        for line in file:
            p_part, v_part = line.split(' ')
            _, pnums = p_part.split('=')
            px, py = pnums.split(',')
            _, vnums = v_part.split('=')
            vx, vy = vnums.split(',')
            lines.append((int(px), int(py), int(vx), int(vy.strip())))
    return lines

def simulate(robots, width, height, seconds):
    final_position = []
    for px, py, vx, vy in robots:
      final_x = (px + (vx * seconds)) % width
      final_y = (py + (vy * seconds)) % height
      final_position.append((final_x, final_y))
    return final_position

def count_in_quadrants(positions, width, height):
    #tl, tr, bl, br
    quad_counts = [0,0,0,0] 
    mx = width // 2
    my = height // 2

    for x,y in positions:
        if x == mx or y == my:
            continue
        
        quad_idx = (
            (1 if x > mx else 0) + 
            (2 if y > my else 0)
        )
        quad_counts[quad_idx] += 1
    return quad_counts

def parse(robots, width=11, height=7, seconds=100):
    final_positions = simulate(robots, width, height, seconds)
    
    quadrants_counts = count_in_quadrants(final_positions, width, height)
    
    safety = 1
    for x in quadrants_counts:
        safety *= x
    return safety

if __name__ == "__main__":
    # file is named 1-input.txt
    lines = parse_input_file('14-input.txt')
    parse(lines)