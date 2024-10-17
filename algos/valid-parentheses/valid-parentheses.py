class Solution:
    def isValid(self, s: str) -> bool:
        """
        approach:
        put opening brackets on theh stack
        compare closing backets against
        what;s on the stack and remove if match

        at end if anything left on stack return false
        """
        stacky = []

        endToStart = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for char in s:
            if char not in endToStart:
                stacky.append(char)
                continue
            if not stacky or stacky[-1] != endToStart[char]:
                return False
            stacky.pop()
        return not stacky
        