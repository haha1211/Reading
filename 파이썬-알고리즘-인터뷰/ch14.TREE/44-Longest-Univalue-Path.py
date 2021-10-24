# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result : int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        # DFS(재귀 이용)

        def dfs(node: TreeNode):

            # leaf node
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            # 자식노드와 부모노드 val 동일한지 확인
            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
    
            self.result = max(self.result, left+right)

            # 단방향 -> 자식노드 중 큰 값 선택
            return max(left, right)
        
        dfs(root)
        return self.result