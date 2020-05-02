const shiftLeft = (string, numTimes) => {
  let arr = string.split('');
  while (numTimes > 0) {
    let shifted = arr.shift();
    arr.push(shifted);
    numTimes -= 1;
  }
  return arr.join('');
}

const shiftRight = (string, numTimes) => {
  let arr = string.split('');
  while (numTimes > 0) {
    let popped = arr.pop();
    arr.unshift(popped);
    numTimes -= 1;
  }
  return arr.join('');
}

const stringShift = (string, matrix) => {
  const prompts = matrix.reduce((acc, curr) => {
    curr[0] === 0 ? acc.left += curr[1] : acc.left -= curr[1];
    return acc;
  }, { left: 0 });

  const res = Math.sign(prompts.left) === 1 ?
    shiftLeft(string, prompts.left) :
    shiftRight(string, Math.abs(prompts.left));

  return res;
}

console.log(stringShift("abc", [[0, 1], [1, 2]]));