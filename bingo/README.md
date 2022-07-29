# B-I-N-G-O

A Bingo card contain 25 squares arranged in a 5x5 grid (five columns and five
rows). Each space in the grid contains a number between 1 and 75. The center
space is marked "FREE" and is automatically filled.

As the game is played, numbers are drawn. If the player's card has that number,
that space on the grid is filled.

A player wins BINGO by completing a row, column, or diagonal of filled spaces.

Your job is to complete the function that takes a bingo card and array of drawn
numbers and return 'true' if that card has achieved a win.

A bingo card will be 25 element array. With the string 'FREE' as the center
element (index 12). Although developers are unscrupulous, they will pass valid
data to your function.
