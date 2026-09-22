struct ListNode *getInteresctionNode(struct ListNode *headA, struct ListNode *headB){
  int lenA = 0;
  int lenB = 0;

  struct ListNode *currA = headA;
  struct ListNode *currB = headB;

  while (currA != NULL){
    lenA++;
    currA = currA->next;
  }

  while (currB != NULL){
    lenB++;
    currB = currB->next;
  }

  currA = headA;
  currB = headB;

  while(lenA > lenB){
    currA = currA -> next;
    lenA--;
  }

  while(lenB > lenA) {
    currB = currB -> next;
    lenB--;
  }

  while (currA != currB){
    currA = currA->next;
    currB = currB->next;
  }

  return currA;
}
