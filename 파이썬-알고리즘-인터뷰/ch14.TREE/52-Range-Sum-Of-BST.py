# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, sum = [root], 0
        
        # DFS (stack 이용) * BFS로도 풀이 가능

        while stack:
            node = stack.pop()
            if node:

                # 조건 해당 X => 가지치기 -> 불필요한 탐색 X & 시간복잡도 향상

                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                
                # 조건에 맞는 값 더하기
                if low <= node.val <= high:
                    sum += node.val
        
        return sum