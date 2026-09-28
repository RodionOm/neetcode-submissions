# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next     # запомнил, кто справа
            curr.next = prev    # стрелку развернул налево
            prev = curr         # prev шагнул вправо
            curr = nxt          # curr шагнул вправо

        return prev