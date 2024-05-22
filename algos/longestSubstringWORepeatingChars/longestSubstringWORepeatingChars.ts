const solution = (s) => {
  // iterate with 2ptr method and add to hash counts
  // if any counts > 1 restart iteration on char
  // whcih is duplicated
  // save longest substring length seen so far
  let chars = new Set();

  let laggingPtr = 0;
  let forwardPtr = 0;
  let maxLen = 0;

  while (forwardPtr < s.length) {
    if (!chars.has(s[forwardPtr])) {
      chars.add(s[forwardPtr]);
      forwardPtr += 1;
      maxLen = Math.max(maxLen, chars.size);
    } else {
      chars.delete(s[laggingPtr]);
      laggingPtr += 1;
    }
  }
  return maxLen;
};

// nndNfdfdf s.length = 0
// set { d, f }
// laggingPtr = 5
// forwardPtr = 6
// max 4
