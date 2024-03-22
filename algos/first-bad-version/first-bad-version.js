/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
 var solution = function(isBadVersion) {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   */
  return function(n) {
      let start = 0;
      let end = n;
      let mid = Math.floor((start+end)/2);
      while (start < end) {
        if (isBadVersion(mid) && !isBadVersion(mid-1)) return mid;
        else if (!isBadVersion(mid) && isBadVersion(mid+1)) return mid+1;
        else if (!isBadVersion(mid)) start = mid;
        else end = mid;
        mid = Math.floor((start + end)/2);
      }
  };
};