/*

Implement a function clamp(number, lower, upper) to restrict a number within the inclusive lower and upper bounds.

Arguments
value (number): The number to clamp.
lower (number): The lower bound.
upper (number): The upper bound.
Returns
(number): Returns the clamped number.

Examples
// Within the bounds, return as-is.
clamp(3, 0, 5); // => 3

// Smaller than the lower bound.
clamp(-10, -3, 5); // => -3

// Bigger than the upper bound.
clamp(10, -5, 5); // => 5

*/

function clamp(value: number, lower: number, upper: number): number {
  if (value >= lower && value <= upper) {
    return value;
  } else if (value < lower) {
    return lower;
  } else {
    return upper;
  }
}
