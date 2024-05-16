package main

 type TreeNode struct {
     Val int
     Left *TreeNode
     Right *TreeNode
 }

 func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	if root.Left == nil && root.Right == nil {
		return [][]int{{root.Val}}
	}

	level := 0
	levels := [][]int{}

	bfs(root, level, &levels)
	return levels
}

func bfs(root *TreeNode, level int, levels *[][]int) {
	if root == nil {
		return
	}
	if len(*levels) == level {
		*levels = append(*levels, []int{})
	}
	(*levels)[level] = append((*levels)[level], root.Val)

	bfs(root.Left, level+1, levels)
	bfs(root.Right, level+1, levels)
}