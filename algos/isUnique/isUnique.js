
// implement an algorithm to determine
// if a list of strings has a duplicate.

function hasDuplicates(names) {
  const occurences = {};

  for (let i = 0; i < names.length; i++) {
    const name = names[i];
    if (occurences[name]) {
      return true;
    }
    occurences[name] = 1;
  }
  return false;
}

console.log(hasDuplicates(["jim", "pam", "toby", "toby"])); //true
console.log(hasDuplicates(["jim", "pam", "michael"])); // false



















// const isUnique = (s) => {
//   const occurences = {};

//   // count occurences of each letter
//   for (let i = 0; i < s.length; i++) {
//     const char = s[i];
//     if (occurences[char]) return false;
//     occurences[char] = 1;
//   }
//   // if any occurence > 1 return false
  
//   return true;
// }


// no additional data structures - n^2
const isUnique = (s) => {
  // loop once over string
    // for each char, loop over all other chars
    // if any other char == char and does not have same index as char, return false
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    for (let j = 0; j < s.length; j++) {
      const otherchar = s[j];
      if (char === otherchar && i !== j) {
        return false;
      }
    }
  }
  
  return true;
};

// console.log(isUnique("abcdefg")); // true
// console.log(isUnique("abcdajkl")); // false