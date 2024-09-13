class Solution:
    def evenFib(self) -> int:
        def fib(val: int) -> int:
            fib_seq = [0,1]

            while True:
                next_fib = fib_seq[-1] + fib_seq[-2]
                if next_fib > val:
                    break
                fib_seq.append(next_fib)

            return fib_seq
        
        fib_seq = fib(4000000)
        print(fib_seq)
        sum = 0

        for val in fib_seq:
            if val % 2 == 0:
                sum += val
        return sum
        
        
sol = Solution()
print(sol.evenFib())