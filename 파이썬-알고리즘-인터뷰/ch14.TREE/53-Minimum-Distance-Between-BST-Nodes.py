# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize
        
        stack = []
        node = root

        # 반복 구조의 중위 순회(left->val->right)
        # 재귀로 구현시 prev, result -> 클래스 멤버 변수로 선언

        while stack or node:
            # left
            while node:
                stack.append(node)
                node = node.left
            
            # val
            node = stack.pop()
            result = min(result, node.val - prev)

            # 비교를 위해 이전 값 prev에 저장
            prev = node.val
            
            # right
            node = node.right
            
        return result