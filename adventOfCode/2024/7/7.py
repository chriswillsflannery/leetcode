from itertools import product


def parse_input_file(filename):
    lines = []
    
    with open(filename, 'r') as file:
        for line in file:
            test_part, numbers_part = line.split(':')
            test_value = int(test_part.strip())
            numbers = [int(x) for x in numbers_part.strip().split()]
            lines.append((test_value, numbers))
    return lines

def get_operator_combinations_recursive(n):
    if n==0:
        return [[]]
    combinations = []
    smaller_combinations = get_operator_combinations_recursive(n-1)
    for combo in smaller_combinations:
        combinations.append(combo + ['+'])
        combinations.append(combo + ['*'])
    return combinations

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i+1]
        else:
            result *= numbers[i+1]
    return result

def can_be_solved(test_value, numbers):
    num_operators_needed = len(numbers) - 1
    possible_operators = get_operator_combinations_recursive(num_operators_needed)
    for operators in possible_operators:
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False
    
def main(lines):
    total = 0
    for test_value, numbers in lines:
        if can_be_solved(test_value, numbers):
            total += test_value
    return total

if __name__ == "__main__":
    # file is named 1-input.txt
    lines = parse_input_file('7-input.txt')
    total = main(lines)
    print(total)