# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 클래스 변수 : longest -> 재할당 위해
    longest: int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # DFS 풀이(재귀 이용)

        def dfs(node: TreeNode) -> int:
            if not node:
                # 리프노드에 -1 부여
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로 (2를 더하는 이유 -> 왼쪽, 오른쪽 자식 노드와의 거리)
            self.longest = max(self.longest, left+right+2)
            # 상태값 : 리프 ~ 현재 노드까지의 거리
            return max(left, right) + 1
        
        dfs(root)
        return self.longest