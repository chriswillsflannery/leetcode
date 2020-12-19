/***************************************************************************
BACKGROUND:
We indicate the factorial of n by n!. It's just the product of the integers 1 through n. For example, 5! equals 1 * 2 * 3 * 4 * 5 or 120.

THE TASK:
Please provide an optimized solution that returns back the product of n!

***************************************************************************/

// Begin your code here

function nFact(n, prod = 1) {
  if (n === 1) return prod;
  prod *= n;
  return nFact((n -= 1), prod);
}

// console.log(nFact(5));

// memoize

const wrapper = () => {
  const memo = {};
  const nFact = (originaln, newn = originaln, prod = 1) => {
    if (memo[originaln]) return memo[originaln];
    if (newn === 1) {
      memo[originaln] = prod;
      return prod;
    }
    prod *= newn;
    return nFact(originaln, (newn -= 1), prod);
  };
  return nFact;
};

const factorial = wrapper();

console.time();
console.log(factorial(5));
console.timeEnd();

console.time();
console.log(factorial(5));
console.timeEnd();
