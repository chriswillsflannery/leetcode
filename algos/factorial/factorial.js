/**

given a series of numbers, calculate factorial of each one.

memoization should be used. Once a value's factorial has been calculated, it should be cached.

In addition to returning the resulting factorial for each number, the count of calculations performed (ie multiplications performed due to lack of cached values) should also be returned to validate that memoization. Each result is returned as a pair [{factorial}, {calculationCount}]

The cache should be reset after each call to solution
The value of 1 should not be considered a calculation since no multiplication is required 

example input
[5,6,3]
result
[[120, 4], [720, 1], [6,0]]

 */

const solution = (numbers) => {
  // Cache to store computed factorials
  const factorialCache = {};
  let calculationCount = 0;

  // Helper function to calculate factorial with memoization
  const factorial = (n) => {
    if (n === 0 || n === 1) {
      return 1;
    }
    if (factorialCache[n]) {
      return factorialCache[n];
    }

    calculationCount += 1;
    factorialCache[n] = n * factorial(n - 1);
    return factorialCache[n];
  };

  // Calculate the factorial for each number in the input array
  const results = numbers.map((num) => {
    calculationCount = 0; // Reset the calculation count for each number
    const result = factorial(num);
    return [result, calculationCount];
  });

  // Reset the cache for the next call
  for (const key in factorialCache) {
    delete factorialCache[key];
  }

  return results;
};
