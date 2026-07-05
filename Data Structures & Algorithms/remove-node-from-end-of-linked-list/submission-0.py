# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes=[]
        curr=head
        while curr:
            nodes.append(curr)
            curr=curr.next
        m=len(nodes)
        remove_idx=m-n
        nodes.pop(remove_idx)

        if not nodes:
            return None

        for i in range(len(nodes)-1):
            nodes[i].next=nodes[i+1]
        nodes[-1].next=None
        head=nodes[0]

        return head


        

        