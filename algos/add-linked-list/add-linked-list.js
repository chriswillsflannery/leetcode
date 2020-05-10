/* You have two numbers represented by linked lists. Each node contains a single digit. The digits
 * are stored in reverse order, such that the 1's digit is at the head of the list. Write
 * a function that adds the two numbers and returns the sum as a linked list with the same
 * structure.
 * EXAMPLE
 * Input: 512, 295 -> (2 -> 1 -> 5) + (5 -> 9 -> 2)
 * Output: 7 -> 0 -> 8
 *
 * The 7 is the ones digit (2 + 5).
 * The 0 is the tens digit (1 + 9, carry the 1).
 * The 8 is the hundreds digit (1 carried over + 5 + 2).
 *
 */

function Node(val) {
  this.value = val;
  this.next = null;
}

function addLL(ll1, ll2) {
  let pointer1 = ll1;
  let pointer2 = ll2;

  let carry;
  while (pointer1 && pointer2) {
    pointer1.value = pointer1.value + pointer2.value;
    if (carry) {
      pointer1.value += carry;
    }
    if (pointer1.value >= 10) {
      carry = pointer1.value % 9;
      pointer1.value = 0;
    } else {
      carry = undefined;
    }
    pointer1 = pointer1.next;
    pointer2 = pointer2.next;
  }
  if (pointer2) {
    pointer1 = new Node(pointer2.value);
  }
  return ll1;
}

const l1 = new Node(2);
l1.next = new Node(1);
l1.next.next = new Node(5);

const l2 = new Node(5);
l2.next = new Node(9);
l2.next.next = new Node(2);

console.log(addLL(l1, l2)); // exp 7 -> 0 -> 8