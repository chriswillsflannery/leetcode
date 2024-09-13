class Solution:
    def largest_prime_factor(self, n):
        # The smallest prime factor
        i = 2
        # The largest prime factor found so far
        largest = 0
        
        # While i * i <= n, we can find prime factors
        while i * i <= n:
            if n % i:
                # If i is not a factor, move to the next number
                i += 1
            else:
                # If i is a factor, divide n by i
                n //= i
                largest = i
        
        # If n > 1, then n is a prime factor itself
        if n > 1:
            largest = n
        
        return largest

sol = Solution()
# print(sol.isPrime(5))
# print(sol.isPrime(7))
# print(sol.isPrime(13))
print(sol.largest_prime_factor(600851475143))