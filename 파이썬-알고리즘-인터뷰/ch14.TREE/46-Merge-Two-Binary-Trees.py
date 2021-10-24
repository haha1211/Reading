# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # 재귀 & 백트래킹

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
       
       # 두 노드 모두 존재할 경우
        if root1 and root2:
            # 후위 순회(Post-Order)
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)          
            return node

        # 그 외 -> 존재하는 노드만 return (둘 다 존재 X시 None return)
        else:
            return root1 or root2