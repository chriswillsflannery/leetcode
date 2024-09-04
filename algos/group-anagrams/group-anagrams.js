class Solution {
  /**
   * @param {string[]} strs
   * @return {string[][]}
   */
  groupAnagrams(strs) {
    /*
          explanation: we have an array of strings.
          for each string we construct a representation of the character count for each string.
          for example, 'cab' becomes [1,1,1,0,0,0,0]
          'abc' is also the same:    [1,1,1,0,0,0,0]
          if we turn this into a string like '#1#1#1#0#0#0
          we can construct an object:
          {
              '#1#1#1#0#0#0': ['cab', 'abc']
          }
          then just return the object values as distinct groups.
      */

    const ans = {};

    for (let s of strs) {
      const occurrences = Array(26).fill(0);
      for (let c of s) {
        occurrences[c.charCodeAt(0) - "a".charCodeAt(0)]++;
      }
      // creates coords like [0,0,1,0] means 'c' exists once

      console.log(occurrences);

      const key = occurrences.join("#");
      console.log(key);
      if (!ans[key]) {
        ans[key] = [];
      }
      ans[key].push(s);
    }

    return Object.values(ans);
  }
}
