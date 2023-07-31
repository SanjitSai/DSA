def search_in_binary_tree_iterative(root, key):
    """
    Search for a key in a binary tree using iteration.

    Parameters:
    root (TreeNode): The root node of the binary tree.
    key: The value to be searched in the binary tree.

    Returns:
    TreeNode or None: The node containing the key if found, or None if the key is not present in the tree.
    """
    if root is None:
        return None

    stack = [root]
    while stack:
        current_node = stack.pop()
        if current_node.key == key:
            return current_node
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return None
