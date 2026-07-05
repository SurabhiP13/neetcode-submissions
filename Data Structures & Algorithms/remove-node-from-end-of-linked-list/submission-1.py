# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        len1=0
        while curr:
            len1+=1
            curr=curr.next
        remove_idx=(len1-n)
        if remove_idx==0:
            return head.next
        itr=0
        curr=head
        while curr:
            if itr==remove_idx-1:
                curr.next=curr.next.next
            itr+=1
            curr=curr.next
        return head
                





        

        