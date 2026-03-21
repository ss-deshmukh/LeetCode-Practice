# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_sum = 0
        count = 0
        l1_curr = l1
        while l1_curr:
            l1_sum += l1_curr.val * pow(10, count)
            l1_curr = l1_curr.next
            count +=1

        l2_sum = 0
        count_2 = 0
        l2_curr = l2
        while l2_curr:
            l2_sum += l2_curr.val * pow(10, count_2)
            l2_curr = l2_curr.next
            count_2 +=1

        res_list = list(str(l1_sum + l2_sum))
        
        result = ListNode(0)
        current = result
        for i in reversed(res_list):
            new_node = ListNode(int(i))
            current.next = new_node
            current = current.next
        
        return result.next
            