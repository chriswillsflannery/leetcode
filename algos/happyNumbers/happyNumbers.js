const isHappy = function (n) {

  if (n === 1) return true;

  if (n === 4) return false;

  const newn = Array.from(String(n), Number);

  const output = newn.reduce((acc, cv) => {
    acc += cv ** 2
    return acc;
  }, 0)

  return isHappy(output);

};