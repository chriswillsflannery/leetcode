def remove_subsumed_tuples(tuple_list):
    # Sort the list based on the start of each range
    sorted_list = sorted(tuple_list, key=lambda x: x[0])
    result = [] # (1,3), (3,4) (5,9)

    #  [(1,3), (3,4), (5,9), (6,7), (10,12)],
    
    for current in sorted_list:
        # If result is empty or current tuple is not subsumed by the last tuple in result
        if not result or current[1] > result[-1][1]:
            # Check if current tuple subsumes any of the previous tuples
            while result and current[0] <= result[-1][0] and current[1] >= result[-1][1]:
                result.pop()
            result.append(current)
    
    return result

# Test cases
test_cases = [
    [(1,3), (3,4), (5,9), (6,7), (10,12)],
    # [(1,3), (1,4), (2,3)],
    # [(1,5), (2,3), (4,7), (6,8), (9,10)],
    # [(1,10), (2,5), (3,7), (4,6), (8,9)]
]

for case in test_cases:
    print(f"Input: {case}")
    print(f"Output: {remove_subsumed_tuples(case)}")
    print()