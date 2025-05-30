from typing import Optional

# 206. Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return None
        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None

        # return newHead
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

# --- Test cases below ---
def list_to_linkedlist(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_reverseList():
    s = Solution()
    # Test empty list
    assert linkedlist_to_list(s.reverseList(None)) == []

    # Test single node
    head = list_to_linkedlist([1])
    assert linkedlist_to_list(s.reverseList(head)) == [1]

    # Test multiple nodes
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    assert linkedlist_to_list(s.reverseList(head)) == [5, 4, 3, 2, 1]

    # Test palindrome list
    head = list_to_linkedlist([1, 2, 2, 1])
    assert linkedlist_to_list(s.reverseList(head)) == [1, 2, 2, 1]

    # Test duplicate values
    head = list_to_linkedlist([1, 1, 1])
    assert linkedlist_to_list(s.reverseList(head)) == [1, 1, 1]

if __name__ == "__main__":
    test_reverseList()
    print("All tests passed.")

