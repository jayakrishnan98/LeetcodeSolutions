class Solution:
    def mergeTwoLists(self, list1, list2):
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