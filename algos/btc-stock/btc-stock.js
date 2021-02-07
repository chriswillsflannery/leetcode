/* given an array of bitcoin prices, where:
  1. indices represent 30min intervals.
  2. values are the price (in US dollars) of one bitcoin at that time.
  3. values are represented as thousands, 40 = $40k. BUT you should return your profit
as its true value, ie. profit of 2 should be returned as 2000.
Write an efficient method that takes BTCPrices and returns the best profit I could have
made from one purchase and one sale of share of bitcoin yesterday.
*/

// const BTCPrices = [40, 39, 37, 39, 41, 40]; 

// getMaxProfit(BTCPrices);
// 4000 -> buy 37, sell 41
// * no shorting - you need to buy before you can sell.
// * you can't buy and sell in the same time step.

const BTCPrices = [40, 39, 37, 39, 41, 40]; 

const getMaxProfit = (BTCPrices) => {
  // init lowestBuySoFar (LBSF) to Inifinity.
  let LBSF = Infinity;
  // init maxProfit to 0
  let maxProfit = 0;
  // if current value is < LBSF, new LBSF becomes value.
  for (let i = 0; i < BTCPrices.length; i++) {
    let curval = BTCPrices[i];
    if (curval < LBSF) {
      LBSF = curval;
    }
    // calc curval - LBSF, if res > maxProfit, new Maxprofit becomes res
    const res = curval - LBSF;
    if (res > maxProfit) {
      maxProfit = res;
    }
  }
  return `${maxProfit * 1000} BTC`;
};

console.log(getMaxProfit(BTCPrices));
var arr1 = [20,10,1,0];
console.log(getMaxProfit(arr1));


// sol
// function getMp(BTCPrices) {
// 	var minIdx = 0;
//   var maxIdx = 1;
//   var currMin = 0;
//   var maxProfit = 0;
  
//   for(var i = 1; i < BTCPrices.length; i++) {
//     let curval = BTCPrices[i];
//       // new current min.
//       if(curval < BTCPrices[currMin]) { 
//         currMin = i;
//       }
//       // new best profit
//       if(BTCPrices[maxIdx] - BTCPrices[minIdx] < curval - BTCPrices[currMin]) {
//               maxIdx = i;
//             minIdx = currMin;
//       }
//   }
//   maxProfit  = BTCPrices[maxIdx] - BTCPrices[minIdx];
//   return maxProfit;
// }

// var arr1 = [10, 7, 5, 8, 11, 9, 1];
// console.log(getMp(arr1));

//The approach we used to solving this problem is also know as a “greedy” approach. Why greedy? At every step of the problem we make the best — or greediest decision available to us at that point. In this case, doing that for every step of the problem will result in the optimal solution in the end.
//Using a “greedy” approach doesn’t always work. In class, we will discuss the traits of greedy problems, and I will elaborate on cases in which they do not provide an optimal solution, and why we may still want to use this approach anyways.