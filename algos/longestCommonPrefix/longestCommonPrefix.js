// n^2 with 0(1) space

// var longestCommonPrefix = function(strs) {
//   // create var to store longest prefix so far
//   let longestSoFar = strs[0] || "";
//   // initialize var as entirety of first word
//   // for each word in array,
//   strs.forEach((word, i) => {
//       for (let j = 0; j < longestSoFar.length; j++) {
//           let letter = longestSoFar[j];
//           if (word[j] !== letter) {
//               //cuttoff point at j
//               longestSoFar = word.slice(0,j);
//               break;
//           }
//       }
//   });
//       // loop over indices of word and var
//       // if letter at indixes don't match up, that is the cutoff point to set
//       // current word sliced from 0 to index as var

//   // return var
//   return longestSoFar;
// };

// n time with 0(1) space

function longestCommonPrefix(strs) {
  if (!strs || strs.length === 0) return "";

  let prefix = strs[0].substr(0); // flow
  let length = prefix.length; // 3
  let arr = strs.slice(1); // [flow, floral]
  let i = 0; // 1

  while (i < arr.length) {
    // 1 < 2
    if (length === 0) return "";
    if (arr[i].substr(0, length) !== prefix) {
      length -= 1;
      prefix = strs[0].substr(0, length);
    } else if (arr[i].substr(0, length) === prefix) {
      i += 1;
    }
  }
  return prefix;
}

const flowers = ["flowers", "flow", "floral"];

console.log(longestCommonPrefix(flowers)); // flo
