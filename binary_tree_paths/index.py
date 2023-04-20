from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path_list = []

        def traversal(root, path: str) -> None:
            if root == None:
                return
            if path == '':
                path = str(root.val)
            else:
                path += '->{}'.format(root.val)
            if root.left == None and root.right == None:
                path_list.append(path)
                return
            traversal(root.left, path)
            traversal(root.right, path)
        traversal(root, '')
        return path_list
