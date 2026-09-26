# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        currHead = ListNode()
        currHead_bak = currHead
        while(list1 and list2):
            if(list1.val <= list2.val):
                if(currHead == None):
                    currHead = list1

                else:
                    currHead.next = list1
                currHead = currHead.next    
                list1 = list1.next
                
            else:
                if(currHead == None):
                    currHead = list2
                else:
                    currHead.next = list2
                currHead = currHead.next    
                list2 = list2.next
        


        while(list1):
            if(currHead == None):
                    currHead = list1
            else:
                    currHead.next = list1
            currHead = currHead.next    
            list1 = list1.next
        

        while(list2):
            if(currHead == None):
                    currHead = list2
        
            else:
                    currHead.next = list2
            currHead = currHead.next    
            list2 = list2.next
        

        return currHead_bak

                
        