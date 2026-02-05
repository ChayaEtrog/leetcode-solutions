# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        index_map = {value: i for i, value in enumerate(inorder)}

        def helper(preL, preR, inL, inR):
            if preL > preR or inL > inR:
                return None

            root_val = preorder[preL]
            root = TreeNode(root_val)

            mid = index_map[root_val]

            left_size = mid - inL

            root.left = helper(
                preL + 1,
                preL + left_size,
                inL,
                mid - 1
            )

            root.right = helper(
                preL + left_size + 1,
                preR,
                mid + 1,
                inR
            )

            return root

        return helper(
            0, len(preorder) - 1,
            0, len(inorder) - 1
        )


        