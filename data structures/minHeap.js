class MinHeap {
  constructor() {
    this.collection = [];
  }

  getLeftChildIndex(parentIndex) {
    return 2 * parentIndex + 1;
  }

  peek() {
    if (!this.collection.length) throw new Error("No collection found");
    return this.collection[0];
  }
}
