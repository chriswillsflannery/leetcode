class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """approach
        check each window in S and keep a hashmap for char count
        if char counts are GT or equal to char counts of T, substring is valid

        construct charcount hashmap of S with all initial values 0
        construct charcount hashmap of T with all counts

        we know that the number of count conditions in T we need to satisfy is 3
        we know we start out with a S count conditions satisfied of 0

        each time we check a window's counts, we say,
        is the S count conditions satisfied >= then the T count conditioned needed to satisfy?
        """

        if t == "": return ""

        countT, window = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        L = 0

        for R in range(len(s)):
            char = s[R]
            window[char] = 1 + window.get(char, 0)
            if char in countT and window[char] == countT[char]:
                have += 1
            while have == need:
                # update result
                sizeOfCurrentWindow = R - L + 1
                if sizeOfCurrentWindow < resLen:
                    res = [L, R]
                    resLen = sizeOfCurrentWindow
                # pop from left of window
                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1
        
        L, R = res
        return s[L:R+1] if resLen != float("infinity") else ""


