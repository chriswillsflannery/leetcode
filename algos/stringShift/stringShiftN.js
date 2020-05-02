const stringShift = (s, shift) => {
  const [shiftLeft, shiftRight] = shift.reduce((acc, curr) => {
    curr[0] ? acc[1] += curr[1] : acc[0] += curr[1];
    return acc;
  }, [0, 0]);
  if (shiftRight === shiftLeft) {
    return s;
  }
  const i = shiftRight > shiftLeft ? s.length - (shiftRight - shiftLeft) % s.length : (shiftLeft - shiftRight) % s.length;
  return s.slice(i) + s.slice(0, i);
};

console.log(stringShift("abc", [[0, 1], [1, 2]]));