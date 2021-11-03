# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    val : int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:

            # right부터 시작하는 중위순회(right->val->left)
            # BST 이므로 항상 오른쪽 값이 자신보다 큼

            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root