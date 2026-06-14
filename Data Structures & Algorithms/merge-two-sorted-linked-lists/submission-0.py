# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        outputList = ListNode(None)
        head = outputList

        while list1 is not None and list2 is not None:

            if list1.val < list2.val:
                outputList.next = list1
                list1 = list1.next
            else:
                outputList.next = list2
                list2 = list2.next
            outputList = outputList.next
        
        outputList.next = list1 or list2
        return head.next
            







        
