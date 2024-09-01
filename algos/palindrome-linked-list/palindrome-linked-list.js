
// Given the head of a singly linked list, return true if it is a
// palindrome
// or false otherwise.

 

// Example 1:

// Input: head = [1,2,2,1]
// Output: true

// Example 2:

// Input: head = [1,2]
// Output: false


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    if (!head || !head.next) return true;
    const nodes = []
    let ptr = head
    while (ptr !== null) {
        nodes.push(ptr.val)
        ptr = ptr.next
    }
    
    let l = 0;
    let r = nodes.length - 1;

    console.log([l,r])
    console.log(nodes)

    while (l < r) {
        if (nodes[l] !== nodes[r]) {
            return false
        }
        l += 1;
        r -= 1;
    }
    return true;
};

// problem with this is 0(n) space complexity?
// is there a way to solve this by modifying the LL in place
// use linked list reversal technique

// fast and slow ptr approach - 2 ptrs
// ptr 1 moves by 1 el
// ptr 2 moves by 2 els
// when ptr2 reaches end of LL we know ptr1 has reached halfway pt
// take 2nd half of LL and create reversed LL
// compare 1st half of original LL against 2nd (reverse) LL

// say we have a LL like head -> n1 -> n2 -> null
// this creates a prev like head -> null
// then new curr is n1 -> n2 -> null
// then prev is like n1 -> head -> null
// then new curr is like n2 -> null
// then prev is like n2 -> n1 -> head -> null
function reverse(head) {
    let prev = null;
    let curr = head;
    while (curr) {
        let next = curr.next
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

var isPalindrome = function(head) {
    let slowptr = head
    let fastptr = head

    while (fastptr && fastptr.next) {
        fastptr = fastptr.next.next
        slowptr = slowptr.next
    }
    
    let rev = reverse(slowptr);
    while (rev) {
        if (head.val !== rev.val) {
            return false
        }
        head = head.next;
        rev = rev.next;
    }
    return true
};