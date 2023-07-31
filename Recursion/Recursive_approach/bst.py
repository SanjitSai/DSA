class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search_in_binary_tree(root, key):
    """
    Search for a key in a binary tree using recursion.

    Parameters:
    root (TreeNode): The root node of the binary tree.
    key: The value to be searched in the binary tree.

    Returns:
    TreeNode or None: The node containing the key if found, or None if the key is not present in the tree.
    """
    if root is None or root.key == key:
        return root

    # Recursively search in the left and right subtrees
    left_result = search_in_binary_tree(root.left, key)
    if left_result:
        return left_result

    right_result = search_in_binary_tree(root.right, key)
    return right_result
