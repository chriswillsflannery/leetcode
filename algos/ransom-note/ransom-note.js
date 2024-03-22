/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
 var canConstruct = function(ransomNote, magazine) {
  const magazineDict = {};
  for (let i = 0; i < magazine.length; i++) {
      const char = magazine[i];
      if (magazineDict[char]) magazineDict[char] += 1;
      else magazineDict[char] = 1;
  }
  for (let i = 0; i < ransomNote.length; i++) {
      const char = ransomNote[i];
      if (magazineDict[char] === 0 || !magazineDict[char]) return false;
      magazineDict[char] -= 1;
  }
  return true;
};

/**
 * alternative
 * var canConstruct = function (ransomNote, magazine) {
  for (const char of magazine) {
    ransomNote = ransomNote.replace(char, "");
  }
  
  return !ransomNote;
};
 */