class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
   }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    if (l1 === null && l2 === null) {
        return null;
    }
    const val1 = l1 ? l1.val : 0;
    const val2 = l2 ? l2.val : 0;
    const sum = val1 + val2;
    const newNode = new ListNode(sum % 10);
    const next1 = l1 ? l1.next : null;
    const next2 = l2 ? l2.next : null;
    if (sum >= 10) {
        const carryNode = new ListNode(1);
        newNode.next = addTwoNumbers(addTwoNumbers(next1, next2), carryNode);
    } else {
        newNode.next = addTwoNumbers(next1, next2);
    }

    return newNode;
};