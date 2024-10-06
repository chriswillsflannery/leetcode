"""
1. Given a string print all subsets (not permutations)

Eg. String "abc" should output
empty string
a
b
c
ab
bc
ac
abc
"""

def print_subsets(s, subset="", index=0):
    # base case: we processed all chars
    if index == len(s):
        print(subset)
        return

    # not including current char
    print_subsets(s, subset, index+1)

    #include current char
    print_subsets(s, subset + s[index], index+1)

input_string = "abc"
print_subsets(input_string)

# for each char in string, we choose to either include it or not.