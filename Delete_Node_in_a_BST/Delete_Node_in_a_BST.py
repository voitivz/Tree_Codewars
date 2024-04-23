# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right
# def array_to_tree(array,index = 0):
#     if index < len(array):
#         node =TreeNode(array[index])
#         node.left = array_to_tree(array, 2 * index + 1)
#         node.right = array_to_tree(array, 2 * index + 2)
#         return node
#     return None
class Solution:
    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # Key is found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Node has two children
            temp = self.find_min(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        
        return root
