var maxProfit = function (prices) {
  let lowestNumSeenSoFar = prices[0];
  let maxProfitMadeSoFar = 0;

  for (let i = 0; i < prices.length; i++) {
    const current = prices[i];
    const profit = current - lowestNumSeenSoFar;
    if (profit > maxProfitMadeSoFar) {
      maxProfitMadeSoFar = profit;
    }
    if (current < lowestNumSeenSoFar) {
      lowestNumSeenSoFar = current;
    }
  }

  return maxProfitMadeSoFar;
};