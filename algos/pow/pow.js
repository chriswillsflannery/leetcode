/* Write a function that calculates x^y, where x is given as the base and y is given as the power.
 * Use recursion!
 */

function powerOf(base, pow, prod = 1) {
  if (pow === 0) return prod;
  prod *= base;
  pow -= 1;

  return powerOf(base, pow, prod);
}

console.log(powerOf(2, 4)) // expect 2 * 2 * 2 * 2 = 16