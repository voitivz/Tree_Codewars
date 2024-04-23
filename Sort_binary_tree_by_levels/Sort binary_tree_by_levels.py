class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def pre_order(node,level = None):
    """
    Traverses a binary tree in pre-order and returns a list of nodes and their levels.

    Args:
        node (Node): The root node of the binary tree.
        level (int, optional): The level of the current node. Defaults to None.
Delete_Node
    Returns:
        list: A list of tuples containing the nodes and their levels. Each tuple has the
        format (node_data, level).
    """
    if not level:
        level = 1
    if not node:
        return []
    lst = [(node.value,level)]
    lst += pre_order(node.left,level + 1)
    lst += pre_order(node.right, level + 1)
    return lst

def tree_by_levels(node):
    lst = pre_order(node,level = None)
    return [i[0] for i in sorted(lst, key=lambda x: x[1])]
print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))