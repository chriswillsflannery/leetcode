
function isEquivalentShallow(a, b) {
  const aKeys = Object.keys(a);
  const bKeys = Object.keys(b);
  if (aKeys.length !== bKeys.length) {
    return false;
  }
  for (let i = 0; i < aKeys.length; i++) {
    let key = aKeys[i];
    if (a[key] !== b[key]) {
      return false;
    }
  }
  return true;
}

function expectEquals(expected, actual) {
  console.log('expected', expected, 'type: ', typeof expected);
  console.log('actual', actual, 'type: ', typeof actual);
  if (expected === actual || isEquivalentShallow(expected, actual)) {
    return `success: expected ${expected}, got ${actual}`;
  } else {
    return `failure: expected ${expected}, got ${actual}`;
  }
}

module.exports = expectEquals;