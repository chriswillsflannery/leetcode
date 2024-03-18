package main

type Stack struct {
	top  int // index for topmost node
	data [100]int
}

func NewStack() *Stack {
	newStack := Stack{}
	newStack.top = -1
	return &newStack
}

func (this *Stack) Push(num int) {
	this.top += 1
	this.data[this.top] = num
}

func (this *Stack) Pop() int {
	if this.top < 0 {
		panic("Invalid operation empty stack")
	}
	tmp := this.data[this.top]
	this.data[this.top] = -1
	this.top--
	return tmp
}

func (this *Stack) isEmpty() bool {
	return this.top == -1
}

func (this *Stack) Peek() int {
	if this.top < 0 {
		panic("Invalid operation empty stack")
	}
	return this.data[this.top]
}

type Queue struct {
	stack1 *Stack
	stack2 *Stack
	front  int
}

func Constructor() Queue {
	return Queue{
		stack1: NewStack(),
		stack2: NewStack(),
		front:  0,
	}
}

func (this *Queue) Push(x int) {
	if this.stack1.isEmpty() {
		this.front = x
	}
	if this.stack1.isEmpty() && this.stack2.isEmpty() {
		this.front = x
	}
	this.stack1.Push(x)
}

func (this *Queue) Pop() int {
	if this.stack2.isEmpty() {
		for !this.stack1.isEmpty() {
			prev := this.stack1.Pop()
			this.stack2.Push(prev)
		}
	}
	return this.stack2.Pop()
}

func (this *Queue) Peek() int {
	if !this.stack2.isEmpty() {
		return this.stack2.Peek()
	}
	return this.front
}

func (this *Queue) Empty() bool {
	return this.stack1.isEmpty() && this.stack2.isEmpty()
}
