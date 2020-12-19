/*

PROVIDED:
  1) A function that returns a random number between 1 and 6
 
TASK:
 1) Build an application that plays the game and ALWAYS wins
 
GAME RULES: 
 1) You will roll a dice a maximum of six times in a row.
 2) Count either the value or 10 * the value of each roll. 
 3) See how close to 101 you can get without going over.
 Ex. 1 or 10, 2 or 20, 3 or 30, etc.

BEFORE WE START:
 1) Imagine rolling a dice on your desk and play through the game with us
 2) Once you understand the rules, you may begin coding below

*/

// Helper function used to generate a random integer between 1 - 6
const generateDiceNumber = () => {
  return Math.floor(Math.random() * 6) + 1;
};

const diceGame = (rolledAmt = 0, total = 0) => {
  if (rolledAmt === 6) return total;
  if (total === 101) return total;

  let currentRoll = generateDiceNumber();
  if (total + currentRoll * 10 <= 101) {
    total += currentRoll * 10;
  } else if (total + currentRoll <= 101) {
    total += currentRoll;
  }
  rolledAmt += 1;

  return diceGame(rolledAmt, total);
};

console.log(diceGame());
