# Pre-order traversal
def pre_order(node):
    if not node:
        return []
    lst = [node.data]
    lst += pre_order(node.left)
    lst += pre_order(node.right)
    return lst

# In-order traversal
def in_order(node):
    if not node:
        return []
    lst = []
    lst += in_order(node.left)
    lst.append(node.data)
    lst += in_order(node.right)
    return lst


# Post-order traversal
def post_order(node):
    if not node:
        return []
    lst = []
    lst += post_order(node.left)
    lst += post_order(node.right)
    lst.append(node.data)
    return lst
