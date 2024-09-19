# given a string consisting of items like *
# and container compartment ends like |
# an array of starting indices
# and an array of ending indices:

# for each pair of starting and ending indices,
# determine the amount of items in closed containers

# Also called "Plates Between Candles"

"""
ex:
s = '|**|*|*
starting = [1,1]
ending = [1,6]

returns [2,3]

Amazon sometimes asks this as a 1-indexed problem rather than 0-indexed so
just something to keep in mind and watch out for.

Approach: 2 pointer left and right at start/end
squeeze inward until found pipes
count stars between bounds
"""
