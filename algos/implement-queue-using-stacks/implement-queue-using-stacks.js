
class MyQueue {
  constructor() {
      this.stack1 = [];
      this.stack2 = [];
  }
  push(x) {
      while (this.stack1.length > 0) {
        this.stack2.push(this.stack1.pop());
      }
      this.stack1.push(x);
      while (this.stack2.length > 0) {
        this.stack1.push(this.stack2.pop());
      }
  }
  pop() {
    return this.stack1.pop()
  }
  peek() {
    return this.stack1[this.stack1.length - 1];
  }
  empty() {
    return this.stack1.length === 0;
  }
}