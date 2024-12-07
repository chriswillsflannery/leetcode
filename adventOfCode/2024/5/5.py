from collections import defaultdict


def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

def parse_input(data):
    if not data:
        raise ValueError('no input data provided')
    selctions = data.split('\n\n')

    if len(selctions) != 2:
        raise ValueError('input data must contain 2 sections')


    rule_section, updates_section = selctions

    #parse rules into a dict of {before: set(after)}
    """
    rules_section like:
    3|1
    2|3
    3|2
    1|2

    rules defaultdict like:
    {
        x: y values must come after x
        3: {1,2},
        2: {3},
        1: {2}
    }
    """
    rules = defaultdict(set)
    for rule in rule_section.split("\n"):
        if '|' in rule:
            # apply int() to each value of [ruleVal1, ruleVal2]
            before, after = map(int, rule.split('|'))
            rules[before].add(after)

    """
    updates section like:
    28,16,25
    79,51,89
    86,65,11

    updates like:
    [
        [28,16,26],
        [79,51,89],
        [86,65,11]
    ]
    """
    updates = []
    for update in updates_section.split('\n'):
        if ',' in update:
            pages = list(map(int, update.split(',')))
            updates.append(pages)
    return rules, updates

"""
positions like:
{ 28: 0, 16: 1, 26: 2 }
{ 79: 0, 51: 1, 89: 2 }
{ 86: 0, 65: 1, 11: 2 }
"""
def is_valid_order(pages, rules):
    positions = {page: idx for idx, page in enumerate(pages)}
    for page in pages:
        if page in rules:
            for must_come_after in rules[page]:
                if must_come_after in positions:
                    if positions[page] >= positions[must_come_after]:
                        return False
    return True

def get_middle_number(pages):
    return pages[len(pages) // 2]

def solve_page_ordering(data):
    if not data:
        raise ValueError('No input data provided')
    
    rules, updates = parse_input(data)
    
    valid_middle_numbers = []
    for update in updates:
        if is_valid_order(update, rules):
            middle = get_middle_number(update)
            valid_middle_numbers.append(middle)

    return sum(valid_middle_numbers)

if __name__ == '__main__':
    filename = '5-input.txt'
    input_data = read_input_file(filename)
    if input_data:
        try:
            result = solve_page_ordering(input_data)
            print(f"Sum of middle numbers from valid updates: {result}")
        except Exception as e:
            print(f"Error processing data: {e}")