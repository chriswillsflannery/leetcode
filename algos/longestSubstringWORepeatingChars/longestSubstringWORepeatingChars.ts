/**
 * Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 */

// find longest substring without repeating characters

type Hash = {
  [char: string]: number
}

function lengthOfLongestSubstring(s: string): number {
    // iterate with 2 pointer method, and add to hash map counts
    // if any counts > 1 restart iteration on char which is duplicated
    // save longest substring length seen so far
    const hash: Hash = {}
    let ptr1 = 0
    let maxLen = 0
    let len = 0

    while (ptr1 < s.length) {
      if (hash[ptr1]) { 
        ptr1 += 1;
        maxLen = Math.max(maxLen, len)
        len = 0;
        continue;
      } else {
        hash[ptr1] = 1;
        len += 1;
      }
    }

    return maxLen
};