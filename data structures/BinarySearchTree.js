/**
 * Construct a binary search tree.
 * It should have available methods:
 * Add a node (with value)
 * Delete a node and all leafs
 * Determine if contains a node
 * Depth First In Order search
 * Depth First Preorder
 * Depth First Post Order
 * Breadth First
 * Min - return minimum stored value
 * Max - return maximum stored value
 */

class Node {
  constructor(val = 0) {
    this.value = val;
    this.left = null;
    this.right = null;
  }
}

class CoolBST {
  constructor(passedRoot = null) {
    this.root = passedRoot;
  }

  /**
   * 
   * @param {number} val 
   * @description adds a node by value search
   * @returns nothing
   */
  add(val = null) {
    const node = new Node(val);
    if (!this.root) this.root = node;
    else {
      let tracker = this.root;
      while (tracker) {
        if (node.value < tracker.value) {
          // go left
          if (!tracker.left) {
            tracker.left = node;
            break;
          }
          tracker = tracker.left;
        } else if (node.value > tracker.value) {
          // go right
          if (!tracker.right) {
            tracker.right = node;
            break;
          }
          tracker = tracker.right;
        } else break;
      }
    }
  }

  /**
   * 
   * @param {number} val
   * @description deletes a node and all its leafs
   * @returns nothing 
   */
  delete(val) {
    if (val === this.root.value) {
      this.root = null;
      return;
    }
    let pointer = this.root;
    while (pointer) {
      if (!pointer) break;
      if (pointer.right.value === val) {
        pointer.right = null;
        break;
      }
      if (pointer.left.value === val) {
        pointer.left = null;
        break;
      }
      if (val < pointer.value) {
        pointer = pointer.left;
      } else if (val > pointer.value) {
        pointer = pointer.right;
      }
    }
  }

  /**
   * 
   * @param {number} val 
   * @description determine if BST contains a value
   * @returns {boolean}
   */
  contains(val) {
    let here = this.root;
    while (here) {
      if (val < here.value) {
        here = here.left;
      } else if (val > here.value) {
        here = here.right;
      } else if (val === here.value) {
        return true;
      } else {
        throw new Error('uh oh...');
      }
    }
    return false;
  }

  /**
   * 
   * @param {function} node 
   * @param {function} callback 
   * @description run callback on all nodes by: Left, Root, Right
   * @returns nothing
   */
  depthFirstInOrder(node, callback) {
    // traverse left and call inorder on node
    if (node) {
      this.depthFirstInOrder(node.left, callback);
      callback(node);
      this.depthFirstInOrder(node.right, callback);
    }
  }

  /**
   * 
   * @param {function} node 
   * @param {function} callback
   * @description run callback on all nodes by: Root, Left, Right
   * @returns nothing 
   */
  depthFirstPreOrder(node, callback) {
    if (node) {
      callback(node);
      this.depthFirstPreOrder(node.left, callback);
      this.depthFirstPreOrder(node.right, callback);
    }
  }

  /**
   * 
   * @param {function} node 
   * @param {function} callback 
   * @description run callback on all nodes by: Left, Right, Root
   * @returns nothing
   */
  depthFirstPostOrder(node, callback) {
    if (node) {
      this.depthFirstPostOrder(node.left, callback);
      this.depthFirstPostOrder(node.right, callback);
      callback(node);
    }
  }

  /**
   * 
   * @param {function} node 
   * @param {function} callback 
   * @description run callback on all nodes LTR in each layer top down
   * @returns nothing
   */
  breadthFirst(node, callback) {
    let topLayer = [node];
    let nextLayer = [];
    while (topLayer[0]) {
      topLayer.forEach(n => {
        if (n.left) {
          nextLayer.push(n.left);
          callback(n.left);
        }
        if (n.right) {
          nextLayer.push(n.right);
          callback(n.right);
        }
      });
      topLayer = nextLayer;
      nextLayer = [];
    }
  }

  /**
   * @description finds minimum value in tree
   * @returns {number | null} value 
   */
  getMin() {
    let curr = this.root;
    let minSoFar = this.root.value;
    while (curr) {
      if (curr.left.value < minSoFar) {
        minSoFar = curr.left.value;
        curr = curr.left;
      }
    }
    return minSoFar;
  }

  /**
   * @description finds max value in tree
   * @returns {number | null} value
   */
  getMax() {
    let curr = this.root;
    let maxSoFar = this.root.value;
    while (curr) {
      if (curr.right.value > maxSoFar) {
        maxSoFar = curr.right.value;
        curr = curr.right;
      }
    }
    return maxSoFar;
  }
}

const bst = new CoolBST();

bst.add(5);
bst.add(3);
bst.add(7);
bst.add(2);
bst.add(4);
bst.add(6);
bst.add(8);
