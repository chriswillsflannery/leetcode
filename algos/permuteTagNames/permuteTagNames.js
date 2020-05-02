/*

given:
const allTags = {
  foo: ['a', 'b'],
  bar: ['c', 'd'],
  baz: ['e', 'f'],
  bee: ['g', 'h']
};

const permuteTagNames = ['foo', 'bar', 'baz'];

function getTagPermutations(allTags, permuteTagNames) {

}

complete the implementation of getTagPermutations dependent on the input permuteTagNames (can be an arbitrary length of items) such that the output for a permuteTagNames of ['foo','bar'] is:

[
  {foo: 'a', bar: 'c'},
  {foo: 'a', bar: 'c'},
  {foo: 'a', bar: 'd'},
  {foo:'b', bar: 'c'},
  {foo: 'b', bar: 'd'}
]

*/

const allTags = {
  foo: ['a', 'b'],
  bar: ['c', 'd'],
  baz: ['e', 'f'],
  bee: ['g', 'h'],
  cob: ['i', 'j']
};

const permuteTagNames = ['foo', 'bar', 'bee'];

// level ['foo'];

function getTagPermutations(allTags, permuteTagNames, level) {
  const results = [];

  function permute(aT, pTN, l, memo = {}) {
    if (Object.keys(memo).length === permuteTagNames.length) {
      results.push(memo);
      return;
    }

    let currentLevel = l[l.length - 1];
    let currentVals = allTags[currentLevel];

    currentVals.forEach(val => {
      memo[currentLevel] = val;
      l.push(permuteTagNames[l.length]);
      permute(aT, pTN, l, { ...memo });
      l.pop();
    })
  }

  permute(allTags, permuteTagNames, level);
  return results;
}

console.log(getTagPermutations(allTags, permuteTagNames, [permuteTagNames[0]]));

// foo         a          b
//
// bar     c      d    c      d