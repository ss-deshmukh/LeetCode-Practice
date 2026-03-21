# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        fin_res = list() 
        curr_que  = deque([root])
        
        while curr_que:
            next_que = deque()
            temp_res = []
            for node in curr_que:
                temp_res.append(node.val)
                if node.left:
                    next_que.append(node.left)
                if node.right:
                    next_que.append(node.right)
            
            curr_que = next_que
            fin_res.append(temp_res)

        return fin_res           
                