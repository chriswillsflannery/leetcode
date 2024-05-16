// given the root of a binary treen return the level order traversal of its nodes values
// from left to right by level

/**
 *
 * ex input = 3
 *         9     20
 *             15   7
 *
 * returns [[3],[9,20],[15,7]]
 */

// class TreeNode {
//      val: number
//      left: TreeNode | null
//      right: TreeNode | null
//      constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//          this.val = (val===undefined ? 0 : val)
//          this.left = (left===undefined ? null : left)
//          this.right = (right===undefined ? null : right)
//      }
//  }

// BFS & remember layer #

function levelOrder(root: TreeNode | null): number[][] {
  // no root node
  if (!root) return [];
  // no child nodes
  if (!root.left && !root.right) return [[root.val]];

  let level = 0;
  const levels: number[][] = [];

  bfs(root, level, levels);

  return levels;
}

function bfs(root: TreeNode | null, level: number, levels: number[][]) {
  if (!root) return null;
  // capture current node
  if (!levels[level]) {
    levels[level] = [root.val];
  } else {
    levels[level].push(root.val);
  }

  bfs(root.left, level + 1, levels);
  bfs(root.right, level + 1, levels);
}
