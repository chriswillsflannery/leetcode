/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
 var hasCycle = function(head) {
   // move both ptrs until fast reaches end or fast and slow meet
  if (!head || !head.next) return false;

  let slow = head; // move 1 step at a time
  let fast = head; // move 2 steps at a time

  while (fast.next && fast.next.next) {
    fast = fast.next.next;
    slow = slow.next;
    if (slow === fast) return true;
  }

  return false;

};

// we use tortoise and hare algorithm to determine 
// if the LL has a cycle, that is, if the last node in the LL
// will return to a previous node in the LL

