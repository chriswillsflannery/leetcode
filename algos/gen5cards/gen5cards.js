const SUITS = [
  "HEARTS",
  "SPADES",
  "CLUBS",
  "DIAMONDS",
];

const CARD_TYPES = [
  "ACE",
  "TWO",
  "THREE",
  "FOUR",
  "FIVE",
  "SIX",
  "SEVEN",
  "EIGHT",
  "NINE",
  "TEN",
  "JACK",
  "QUEEN",
  "KING",
];

// BRUTE FORCE SOLUTION

const allCards = SUITS.reduce((acc, curr) => {
  CARD_TYPES.forEach(type => acc.push(`${type} ${curr}`));
  return acc;
}, ["JOKER1", "JOKER2"]);

const getRandomNumber = (max) => {
  return Math.floor(Math.random() * Math.floor(max));
}

const pullCards = (allCards) => {
  const returnCards = [];
  for (let i = 0; i < 5; i++) {
    const index = getRandomNumber(51);
    const card = allCards[index];
    allCards.splice(index, 1);
    returnCards.push(card);
  }
  return returnCards;
}

// console.log(pullCards(allCards));

// ALTERNATE SOLUTION

//  generate random card combo, put in set
// if random generation already exists in set, skip

const gen5Cards = () => {
  const cards = new Set([]);
  while (cards.size < 5) {
    const randomCard = CARD_TYPES[getRandomNumber(13)];
    const randomSuit = SUITS[getRandomNumber(3)];
    const newCard = `${randomCard} ${randomSuit}`;
    if (!cards.has(newCard)) cards.add(newCard);
  }
  return cards;
}

// console.log(gen5Cards());