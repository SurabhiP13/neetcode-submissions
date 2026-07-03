# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        ptrs={}
        while curr:
            if curr.next in ptrs:
                return True
            ptrs[curr.next]=curr.val
            curr=curr.next
        return False

        