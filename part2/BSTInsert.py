# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def helper(root, val):
    if root == None:
        # now we add the  element
        return
    # base cases
    if root.val < val and root.right == None:
        root.right = TreeNode(val)
        return
    elif root.val > val and root.left == None:
        root.left = TreeNode(val)
    # recursion
    if root.val < val:
        # go to the right substree
        helper(root.right, val)
    elif root:
        helper(root.left, val)


def recBstInsert( root, val):
    helper(root, val)
    return root

def insertIntoBST( root, val):
    """
            :type root: TreeNode
            :type val: int
            :rtype: TreeNode
            """

    # first find where to insert the node
    current = root
    if current == None:
        return None
    while (current != None):
        print("running")
        if current.val > val and current.left != None:
            current = current.left
            continue
        elif current.val < val and current.right != None:
            current = current.right
            continue
        # base cases
        if current.val > val and current.left == None:
            print("adding")
            current.left = TreeNode(val)
            break
        elif current.val < val and current.right == None:
            current.right = TreeNode(val)
            break
    return root




