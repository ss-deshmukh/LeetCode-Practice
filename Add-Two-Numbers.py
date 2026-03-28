1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        l1_sum = 0
9        count = 0
10        l1_curr = l1
11        while l1_curr:
12            l1_sum += l1_curr.val * pow(10, count)
13            l1_curr = l1_curr.next
14            count +=1
15
16        l2_sum = 0
17        count_2 = 0
18        l2_curr = l2
19        while l2_curr:
20            l2_sum += l2_curr.val * pow(10, count_2)
21            l2_curr = l2_curr.next
22            count_2 +=1
23
24        res_list = list(str(l1_sum + l2_sum))
25        
26        result = ListNode(0)
27        current = result
28        for i in reversed(res_list):
29            new_node = ListNode(int(i))
30            current.next = new_node
31            current = current.next
32        
33        return result.next
34            