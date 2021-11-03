# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # 전위 순회 결과는 중위 순회 분할 index
            # 전위 순회 첫번째 값 = root / 중위 순회에서 그 값 기준으로 왼쪽은 left 위치 오른쪽은 right 위치
            # 다른 노드들도 마찬가지 => 재귀로 풀이

            index = inorder.index(preorder.pop(0))
            
            # 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            
            return node