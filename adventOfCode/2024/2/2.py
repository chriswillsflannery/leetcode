"""
--- Day 2: Red-Nosed Reports ---

Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

"""

"""
for each line:
1 2 3 4 5
report is safe if all increasing or all decreasing
must either increase or decrease by at least 1, at most 3
every adjacent must either increase or decrease

hint
it doesn't matter if sequence is increasing or decreasing
when comparing 2 adjacent numbers we only care about their difference
then later we can check if all diffs are conssistenly
increasing or decreasing
"""

def parse_input(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.strip().split()
            line = [int(num) for num in numbers]
            lines.append(line)
    return lines

def is_valid_sequence(sequence):
    diffs = []
    for i in range(1, len(sequence)):
        diff = sequence[i] - sequence[i-1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        diffs.append(diff)
    return all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)

def main(numbers):
    num_safe = 0
    for sequence in numbers:
        if is_valid_sequence(sequence):
            num_safe += 1
    return num_safe

#### part two

"""
if by removing one (bad) value from a sequence, this makes the sequence safe,
then we can call that sequence safe.

For example, in the original problem, this sequence was unsafe:
[1,2,9,3,4]
But if we remove 9, the sequence becomes:
[1,2,3,4] and it is now safe

For example, in the original problem, this sequence was unsafe:
[1,2,6,7,8]
And even if we remove any value, it is still unsafe.

examples:

seq [1,2,3,4,10]
diffs [1,1,1,6]
-remove 6 to make valid
-we remove first jump greater than 3

seq [1,10,3,4,5]
diffs [9,-7,1,1]
- remove 10, but here, we have to recompute diffs

how do we know to remove a value because its diff is opposite sign, or because it's < 1 || > 3?

Run through a sequence.
[1,-2,3,4,5]
For example here, how do we know that -2 is the rulebreaker?

we can brute force this by testing:
if sequence is valid
OR
if sequence is valid after removing value, for each value in sequence

"""

def safe_after_removing_one_val(sequence):
    for i in range(len(sequence)):
        modified_sequence = sequence[:i] + sequence[i+1:]
        if is_valid_sequence(modified_sequence):
            return True
    return False

def main2(numbers):
    num_safe = 0
    for sequence in numbers:
        if is_valid_sequence(sequence) or safe_after_removing_one_val(sequence):
            num_safe += 1
    return num_safe


if __name__ == '__main__':
    numbers = parse_input('2-input.txt')
    res = main(numbers)
    print(res)

    res2 = main2(numbers)
    print(res2)
