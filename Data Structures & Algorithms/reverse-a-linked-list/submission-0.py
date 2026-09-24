# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next     # 1. запомнили дорогу вперёд
            curr.next = prev    # 2. развернули стрелку назад
            prev = curr         # 3. сдвинули prev
            curr = nxt          # 4. сдвинули curr

        return prev