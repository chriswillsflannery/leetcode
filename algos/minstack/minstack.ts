// implement minstack class which has the following methods
// push, pop, top, and min element in constant time

class MinStack {
  public minElementStack: number[];
  public stack: number[];
  constructor() {
    this.minElementStack = [];
    this.stack = [];
  }

  push(el: number) {
    this.stack.push(el);
    this.minElementStack.push(
      Math.min(this.minElementStack[this.minElementStack.length - 1], el)
    );
  }
  pop() {
    this.minElementStack.pop();
    return this.stack.pop();
  }
  top() {
    return this.stack[this.stack.length - 1];
  }
  minElement() {
    return this.minElementStack[this.minElementStack.length - 1];
  }
}
