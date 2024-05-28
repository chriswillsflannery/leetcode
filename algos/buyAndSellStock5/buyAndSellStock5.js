/**
 You are given an integer array prices where prices[i]
 is the price of a given stock on the ith day.
 
On each day, you can complete 1 transaction You may either:
1. Buy one share of stock at the current price
2. Sell as many of your current shares of stock as you wish, at the current price
3. Do nothing
 
 Input: prices = [7,1,5,3,6,4]

 Buy low sell high!

 explanation:
 Do nothing on 7.
 Buy 1 share on 1. Total profit -1, total shares 1
 Sell 1 share on 5. Total profit 4, total shares 0
 Buy 1 share on 3. Total profit 1, total shares 1
 Sell 1 share on 6. Total profit 7, total shares 0
 Do nothing on 4.
End total profit 7.
 */

// find minimum so far. buy low sell high
// I dont think you would ever want to sell, but not sell ALL your shares.

function maxProfit(prices) {
  let totalProfit = 0;
  let totalShares = 0;

  // init i to 1 because we will always compare against previous element
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > prices[i - 1]) {
      // if current price is higher than the previous price
      // sell [all?] shares we currently have
      totalProfit += totalShares * prices[i];
      totalShares = 0;
    } else {
      // buy one share
      totalShares += 1;
      totalProfit -= prices[i];
    }
  }

  // still have shares left to sell at end
  totalProfit += totalShares * prices[prices.length - 1];
  return totalProfit;
}

// alternative solution
/**
 * first look this is wrong i think.  What you wanna do is for every price know whats the biggest value to the right of it if there is one always buy on that day if not sell everything you have on all of those days.  So for your example biggest profit is actually 9 you'd buy on 1 5 and 3 and sell them all on 6 and have 9 profit total.
so just loop through array backwards and make a new array of like biggest number to the right of i and keep track of maximum and put that at every index.  Then loop forwards to determine profit
Give you O(n) solution.
 */

function stockmax(prices: number[]): number {
  let maxNum = -1;
  //Array of best number to sell at
  const sellPrice = new Array(prices.length).fill(-1);
  for (let i = prices.length - 1; i >= 0; i--) {
    sellPrice[i] = maxNum;
    maxNum = Math.max(maxNum, prices[i]);
  }
  let res = 0;
  let shares = 0;
  for (let i = 0; i < prices.length; i++) {
    //If best number to sell at is bigger than current price we buy
    if (sellPrice[i] > prices[i]) {
      res -= prices[i];
      shares += 1;
      //No number bigger than this price in the future so we sell
    } else {
      res += prices[i] * shares;
      shares = 0;
    }
  }
  return res;
}
