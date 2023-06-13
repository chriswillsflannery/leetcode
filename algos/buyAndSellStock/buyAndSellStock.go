func maxProfit(prices []int) int {
	greatestProfitSoFar := 0
	lowestNumSeenSoFar := prices[0]

	for _, price := range prices {
		if (price - lowestNumSeenSoFar) > greatestProfitSoFar {
			greatestProfitSoFar = price - lowestNumSeenSoFar
		}
		if price < lowestNumSeenSoFar {
			lowestNumSeenSoFar = price
		}
	}

	return greatestProfitSoFar
}