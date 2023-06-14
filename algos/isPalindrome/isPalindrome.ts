var isPalindrome = function (s) {
  const anmc = 'abcdefghijklmnopqrstuvwxyz0123456789';
  const alteredString = s.replace(/[^a-zA-Z0-9]/g, "");
  return alteredString.toLowerCase() === alteredString.split('').reverse().join('').toLowerCase();
};