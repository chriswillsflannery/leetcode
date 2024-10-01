/*

Given a previous portfolio:
{
    MSFT: 50,
    SPOT: 100,
}

And given a desired portfolio:
{
    MSFT: 75,
    SPOT: 75,
}

Create a function which returns a list of all the trades necessary to reach a "desired" portfolio.
The list of trades for the above would be:
[
{ from: SPOT, to: MSFT, amount: 25 }
]

Here's another example:
Previous portfolio:
{
    MSFT: 50,
    SPOT: 100,
}
Desired portfolio:
{
    MSFT: 50,
    SPOT: 50,
    WMT: 50
}
*/

function calculateTrades(previousPortfolio, desiredPortfolio) {
    const trades = [];
    const sellStocks = {};
    const buyStocks = {};

    // Calculate differences
    for (const stock in previousPortfolio) {
        const diff = (desiredPortfolio[stock] || 0) - previousPortfolio[stock];
        if (diff < 0) {
            sellStocks[stock] = Math.abs(diff);
        } else if (diff > 0) {
            buyStocks[stock] = diff;
        }
    }

    // Add new stocks to buy
    for (const stock in desiredPortfolio) {
        if (!(stock in previousPortfolio)) {
            buyStocks[stock] = desiredPortfolio[stock];
        }
    }

    // Match sells with buys
    for (const sellStock in sellStocks) {
        let amountToSell = sellStocks[sellStock];
        for (const buyStock in buyStocks) {
            if (amountToSell === 0) break;
            
            const amountToBuy = buyStocks[buyStock];
            const tradeAmount = Math.min(amountToSell, amountToBuy);
            
            if (tradeAmount > 0) {
                trades.push({ from: sellStock, to: buyStock, amount: tradeAmount });
                amountToSell -= tradeAmount;
                buyStocks[buyStock] -= tradeAmount;
                
                if (buyStocks[buyStock] === 0) {
                    delete buyStocks[buyStock];
                }
            }
        }
    }

    return trades;
}

// Test cases
const previousPortfolio1 = { MSFT: 50, SPOT: 100 };
const desiredPortfolio1 = { MSFT: 75, SPOT: 75 };
console.log(calculateTrades(previousPortfolio1, desiredPortfolio1));

const previousPortfolio2 = { MSFT: 50, SPOT: 100 };
const desiredPortfolio2 = { MSFT: 40, SPOT: 50, WMT: 60 };
console.log(calculateTrades(previousPortfolio2, desiredPortfolio2));