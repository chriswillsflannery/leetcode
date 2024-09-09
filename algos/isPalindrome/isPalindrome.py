class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use isalnum for is alphanumeric
        alpha = ''.join(e for e in s if e.isalnum()).lower()

        reverse = alpha[::-1]
        if alpha == reverse:
            return True
        else:
            return False