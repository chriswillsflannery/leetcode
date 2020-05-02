var maxProfit = function (prices) {
  let totalProfit = 0;
  let minVal = Infinity;
  let localProfit = 0;

  for (let i = 0; i < prices.length; i++) {
    if (prices[i] - minVal < localProfit) {
      totalProfit += localProfit;
      localProfit = 0;
      minVal = Infinity;
    }
    if (prices[i] < minVal) minVal = prices[i];
    if (prices[i] - minVal > localProfit) {
      localProfit = prices[i] - minVal;
    }
  }
  if (localProfit > 0) totalProfit += localProfit;
  return totalProfit;

};

console.log('maxtest', maxProfit([1, 2, 3, 4, 5]))