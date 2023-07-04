/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, color) {
  if (image.length === 0) return image;
  const startColor = image[sr][sc];
  if (startColor === color) return image;
  dfs(image, sr, sc, startColor, color);
  return image;
};
function dfs(image, x, y, startColor, toColor) {
  if (x < 0 || y < 0 || x >= image.length || y >= image[x].length) return;
  if (image[x][y] === startColor) {
    image[x][y] = toColor;
  } else {
    return;
  }
  dfs(image, x + 1, y, startColor, toColor); //bottom
  dfs(image, x - 1, y, startColor, toColor); //top
  dfs(image, x, y + 1, startColor, toColor); // right
  dfs(image, x, y - 1, startColor, toColor); // left
}



