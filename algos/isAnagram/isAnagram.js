function isAnagram(s, t) {
  // fill object with occurences of string1
  // remove object with occurences of string2
  // anything left over, is not anagram

  const obj = {};

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    obj[char] ? obj[char] += 1 : obj[char] = 1;
  }

  for (let i = 0; i < t.length; i++) {
    const char = t[i];
    obj[char] -= 1;
  }

  return Object.values(obj).every((val) => val === 0);
}