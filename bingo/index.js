
/**
 * B-I-N-G-O
 *
 * A Bingo card contain 25 squares arranged in a 5x5 grid (five columns
 * and five rows). Each space in the grid contains a number between 1
 * and 75. The center space is marked "FREE" and is automatically filled.
 *
 * As the game is played, numbers are drawn. If the player's card has
 * that number, that space on the grid is filled.
 *
 * A player wins BINGO by completing a row, column, or diagonal of filled
 * spaces.
 *
 * Your job is to complete the function that takes a bingo card and array
 * of drawn numbers and return 'true' if that card has achieved a win.
 *
 * A bingo card will be 25 element array. With the string 'FREE' as the
 * center element (index 12). Although developers are unscrupulous, they
 * will pass valid data to your function.
 */

// BRUTE FORCE METHOD 1

// we want something that looks like:
/*
  {
    8 => { position: '0-0', hasBeenCalled: false },
    29 => { position: '0-1', hasBeenCalled: false },
  }
*/
const createBingoMatrix = (board) => {
  const matrix = new Map;
  board.forEach((entry, idx) => {
    let row = Math.floor(idx/5);
    let col = idx % 5;
    let position = `${row}-${col}`;
    matrix.set(entry, {
      position,
      hasBeenCalled: entry === 'FREE' ? true : false,
    });
  });
  return matrix;
}

// we want something that looks like:
/*
  {
    8 => { position: '0-0', hasBeenCalled: false },
    29 => { position: '0-1', hasBeenCalled: true },
  }
*/
const recordDrawnNumbersInMatrix = (drawnNumbers, matrix) => {
  drawnNumbers.forEach(value => {
    if (matrix.get(value)) {
      matrix.set(value, {
        ...matrix.get(value),
        hasBeenCalled: true,
      });
    }
  });
  return matrix;
}

// we want something that looks like:
/*
[
  Set(3) { '0-0', '1-1', '4-4' },
  Set(2) { '3-1', '1-3' }
]
*/
const reducePossibleWins = (possibleWins, matrixWithDrawnNumbers) => {
  matrixWithDrawnNumbers.forEach(entry => {
    if (entry.hasBeenCalled) {
      possibleWins.forEach(winCombo => {
        winCombo.delete(entry.position);
      });
    }
  });
  return possibleWins;
}

const checkForBingo = (bingoCard, drawnNumbers) => {
  // determine all possible win structures
  const possibleWins = [
    // column wins
    new Set(['0-0', '1-0', '2-0', '3-0', '4-0']),
    new Set(['0-1', '1-1', '2-1', '3-1', '4-1']),
    new Set(['0-2', '1-2', '2-2', '3-2', '4-2']),
    new Set(['0-3', '1-3', '2-3', '3-3', '4-3']),
    new Set(['0-4', '1-4', '2-4', '3-4', '4-4']),
    // row wins
    new Set(['0-0', '0-1', '0-2', '0-3', '0-4']),
    new Set(['1-0', '1-1', '1-2', '1-3', '1-4']),
    new Set(['2-0', '2-1', '2-2', '2-3', '2-4']),
    new Set(['3-0', '3-1', '3-2', '3-3', '3-4']),
    new Set(['4-0', '4-1', '4-2', '4-3', '4-4']),
      // diagonal wins
    new Set(['0-0', '1-1', '2-2', '3-3', '4-4']),
    new Set(['4-0', '3-1', '2-2', '1-3', '0-4']),
  ];

  // construct matrix
  const matrix = createBingoMatrix(bingoCard);
  // log drawn numbers
  const matrixWithDrawnNumbers = recordDrawnNumbersInMatrix(drawnNumbers, matrix);
  // reduce our possible wins Sets based on what was drawn
  const reducedPossibleWins = reducePossibleWins(possibleWins, matrixWithDrawnNumbers);

  // check reduced Sets - if any is empty, we have a win
  return reducedPossibleWins.some(combo => combo.size === 0);
}

module.exports = checkForBingo;

// this should return true with diagonal + free
console.time();
console.log(checkForBingo(
  [
    8, 29, 35, 54, 65,
    13, 24, 44, 48, 67,
    9, 21, 'FREE', 59, 63,
    7, 19, 34, 53, 61,
    1, 20, 33, 46, 72
  ],
  [
    8, 24, 53, 72
  ]
));
console.timeEnd();

// this should return false
console.time();
console.log(checkForBingo(
  [
   8, 29, 35, 54, 65,
   13, 24, 44, 48, 67,
   9, 21, 'FREE', 59, 63,
   7, 19, 34, 53, 61,
   1, 20, 33, 46, 72
  ],
  [
    1, 33, 53, 65, 29, 75
  ]
));
console.timeEnd();

/* 

Developer's note - this solution runs in n^2 time.
In a real world scenario with larger data sets it would be worth exploring
whether there is a way to achieve this in linear time.

Some considerations: 
The data sets provided here are quite small (and we can assume that in a real life game of
bingo there would probably be no more than 10-15 calls before a participant
has a bingo), so quadratic runtime here is negligible. Of course, in many real world applications
we are working with significantly larger data sets.
The average logged run time of a "cold start" of this solution is about 4ms.
The average logged run time of a "warm start" ie. the second, and subsequent invocations
of checkForBingo, is about 0.2ms. (With some variation depending on your runtime, that
is - I am working in Coderpad which I believe runs Node under the hood)

I think there is probably some kind of very elegant way to achieve an even faster solution
using a graph, i.e.:
- create a relationship between each space on the board and its adjacent spaces which are
required to complete a winning row/col/diagonal.
- for each number in drawnNumbers, recursively traverse the graph and "cross off" used spaces
as you go.
- finally, check if any winning rol/col/diagonal is completely "crossed off".
*/
