/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
	// get maxDepth of left
	// get maxDepth of right
	// if dif > 1 return false
	if root == nil {
		return true
	}
	dif := maxDepth(root.Left) - maxDepth(root.Right)
	if dif <= 1 && dif >= -1 {
		return isBalanced(root.Left) && isBalanced(root.Right)
	}
	return false
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return max(maxDepth(root.Left), maxDepth(root.Right)) + 1
}

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}