/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 * For example. given:
 * input: 1->2->4, 1->3->4
 * return: 1->1->2->3->4->4
 */
// solution in-place
function mergeTwoLists(l1, l2) {
  // traverse l1 and l2 concurrently. for each node in l1, point its NEXT to
  // current node in l2. Also remember to save refence to original l1 node's next.
  // point current l2 node at 'remembered' l1 next.
  // repeat this process for l2.
  let pointer1 = l1;
  let pointer2 = l2;

  while (pointer1 && pointer2) {
    let prev1Next = pointer1.next;
    pointer1.next = pointer2;
    pointer1 = prev1Next;
    let prev2Next = pointer2.next;
    pointer2.next = pointer1;
    if (!pointer1 && prev2Next) {
      pointer2.next = prev2Next;
      return l1;
    }
    pointer2 = prev2Next;
  }
  // if l1 is longer than l2
  if (pointer1 && !pointer2) {
    return l1;
  }
}

// using additional LL
var mergeTwoLists = function (l1, l2) {
  let list = new ListNode();
  let head = list;

  while (l1 !== null && l2 !== null) {
    // Select the smallest value from either linked list,
    // then increment that list forward.
    if (l1.val < l2.val) {
      list.next = new ListNode(l1.val);
      l1 = l1.next;
    } else {
      list.next = new ListNode(l2.val);
      l2 = l2.next;
    }

    list = list.next;
  }

  // It's possible that one linked list is shorter than the other so we just
  // add on the remainder of the last linked list. It's already sorted :)
  if (l1 !== null) list.next = l1;
  if (l2 !== null) list.next = l2;

  // return .next because this first element in the linkedlist is empty
  return head.next;
};
