def parse_input(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip()
            lines.append(row)
    return lines