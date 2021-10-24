# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # DFS (stack 이용) / BFS로도 풀이 가능 -> Top-Down

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                # 전위 순회(Pre-Order) / 순서 바꿔서 후위 순회(Post-Order)로도 풀이 가능

                node.left, node.right = node.right, node.left
                
                stack.append(node.left)
                stack.append(node.right)
                
        return root