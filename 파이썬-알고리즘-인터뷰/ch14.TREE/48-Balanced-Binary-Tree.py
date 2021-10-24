# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Height-Balanced : 모든 노드의 서브 트리 간의 높이 차이가 1 이하인 것

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # 재귀 구조로 Height 차이 계산

        def check(root):

            # leaf node
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            
            # 높이 차이 나는 경우 -> -1(한 번이라도 차이가 1 초과할 경우 계속해서 -1 return 됨)
            # 이외에는 Height에 따라 1 증가
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1
        
        return check(root) != -1