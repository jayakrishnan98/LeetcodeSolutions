# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        
        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = None if i+1 == len(lists) else lists[i+1]
                merged_list.append(self.merge_linked_list(l1, l2))
            lists = merged_list

        return lists[0] if lists else None

    def merge_linked_list(self, list1, list2):
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val > list2.val:
                current.next = ListNode(list2.val)
                list2 = list2.next
            else:
                current.next = ListNode(list1.val)
                list1 = list1.next
            current = current.next
            
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next
