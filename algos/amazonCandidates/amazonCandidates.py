"""
Candidates are asked to sort the permutation p of length n.
The ith candidate sorted the permutation in moves[i] moves.

Given the original permutation array p and the numbner of moves
made by each of the candidates, 
find whether you can sort the permutation p by performing exactly
moves[i] moves.

In one move you can swap 2 values.

Example
n = 4, p = [2,3,1,4], q = 2, moves = [2,3]

in first query moves[0], we can sort the p using 2 moves
[2,3,1,4]
[1,3,2,4]
[1,2,3,4]

in the first query moves[1], we can show that it's not possible
to sort the p using 3 moves.

return the answer, ie. [2,3] -> [true, false] as a binary string:
"10"
"""
