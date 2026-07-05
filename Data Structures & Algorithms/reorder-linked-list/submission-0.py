# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr=head
        ptrs=[]
        while curr:
            ptrs.append(curr)
            curr=curr.next
        
        l, r=0, len(ptrs)-1
        
        while l<r:
            ptrs[l].next=ptrs[r]
            l+=1
            if l>=r:
                break
            ptrs[r].next=ptrs[l]
            r-=1

        ptrs[l].next=None
    
