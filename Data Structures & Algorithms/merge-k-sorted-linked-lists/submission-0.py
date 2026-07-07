# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k=len(lists)
        dummy=node=ListNode()

        lists_arr=[]
        for i in range(k):
            curr=lists[i]
            while curr:
                lists_arr.append(curr)
                curr=curr.next

        lists_arr.sort(key= lambda x: x.val)

        for lis in lists_arr:
            node.next=lis
            node=node.next
        node.next=None
        return dummy.next

        
        


        