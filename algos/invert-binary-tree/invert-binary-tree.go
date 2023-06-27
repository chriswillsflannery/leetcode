/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
	// start at root

	if root == nil {
		return root
	}

	// assign current leftnode to be rightnode
	// assign current rightnode to be leftnode
	curr := root.Left
	root.Left = root.Right
	root.Right = curr

	// traverse left
	// re-perform above
	invertTree(root.Left)

	// traverse right
	// re-perform above
	invertTree(root.Right)

	return root
}