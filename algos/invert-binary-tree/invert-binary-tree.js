/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     root.val = (val===undefined ? 0 : val)
 *     root.left = (left===undefined ? null : left)
 *     root.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {
  // start at root

  // if there's no left and no right,
  // return
  if (root == null) return root;

  // assign current leftnode to be rightnode
  let tempNode = root.left;
  root.left = root.right;
  // assign current rightnode to be leftnode
  root.right = tempNode;

  // traverse left
  // re-perform above
  invertTree(root.left);

  // traverse right
  // re-perform above
  invertTree(root.right);

  // return root
  return root;
};