# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res,stack=[],[]
        curr=root

        while curr or stack:
            if curr:
                stack.append((curr, False))
                curr = curr.left
            else:
                node, visited = stack.pop()
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    curr = node.right

        return res
        