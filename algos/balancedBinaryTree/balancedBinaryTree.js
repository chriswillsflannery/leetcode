function isBalanced(root) {
  if (!root) return true;
  return height(root) !== -1;
}

function height(root) {
  if (!root) return 0;
  let leftHeight = height(root.left);
  let rightHeight = height(root.right);
  if (leftHeight === -1 || rightHeight === -1) return -1;
  // if heights differ more than 1 return -1
  if (Math.abs(leftHeight - rightHeight) > 1) return -1;
  // otherwise return height of this subtree
  return Math.max(leftHeight, rightHeight) + 1;
}