# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0
        
        #BFS풀이(queue 이용)

        while queue:
            depth += 1

            # 부모 노드 길이 만큼만 반복 -> 자식노드와 섞이지 X
            # queue 연산 추출 노드(부모 노드)의 자식 노드 삽입
            for _ in range(len(queue)): 
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수 == 깊이         
        return depth