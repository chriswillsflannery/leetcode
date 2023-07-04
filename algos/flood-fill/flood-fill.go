func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	if len(image) == 0 {
		return image
	}
	startColor := image[sr][sc]
	if startColor == color {
		return image
	}
	dfs(image, sr, sc, startColor, color)
	return image
}
func dfs(image [][]int, x int, y int, startColor int, toColor int) [][]int {
	if x < 0 || y < 0 || x >= len(image) || y >= len(image[x]) {
		return nil
	}
	if image[x][y] == startColor {
		image[x][y] = toColor
	} else {
		return nil
	}
	dfs(image, x-1, y, startColor, toColor)
	dfs(image, x+1, y, startColor, toColor)
	dfs(image, x, y-1, startColor, toColor)
	dfs(image, x, y+1, startColor, toColor)
	return nil
}