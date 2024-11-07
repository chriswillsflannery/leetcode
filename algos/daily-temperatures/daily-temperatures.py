class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        if we calculate difference:
        temps = [30,38,30,36,35,40,28]
        output= [1, 4,  1, 2, 1, 0, 0]

        explanation:
        index == 0
        temps == 30
        next higher temp is 38, which is 1 day after index 0

        solution:
        stack in monotonic decreasing order; example:
        push 73
        push 72
        push 71
        encounter 72 -> this is greater than top of stack (71)
        so we pop 71
        push 72

        so for our example:
        push 30 [30]
        encounter 38, pop 30, push 38 [38]
        push 30 [30, 38]
        encounter 36, pop 30, push 36 [36,38]
        push 35 [35,36,38]
        encounter 40, pop 35, pop 36, pop 38, push 40 [40]
        push 28 [28, 40]

        so for any number, the output is basically:
        how many "rounds" did this number last on the stack, before
        it got popped off?
        30 lasted one round.
        38 lasted 4 rounds
        etc.
        '''
        output = [0] * len(temperatures)
        stack = [] # pair like [temp,index]

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                output[stackInd] = (i-stackInd)
            stack.append([t,i])
        return output
            
