# In your own words, describe an algorithm that uses the properties of a
# # BST to take in a list of unsorted elements and output a list of sorted elements.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#  using the insert bst function for this problem


def insertIntoBST(self, root, val):
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
def inorder ( root , myList):

    if root == None:
        return
    if root.left == None and root.right == None:
        myList.append(root.val)
        return
    inorder(root.left, myList)
    myList.append(root.val)
    inorder(root.right,myList)

# this is my function / work Sort it !
# TODO this needs to be better tested
def sortIt ( unSortedLst ):
    """
    :param unSortedLst:
    :return: sorted list
    """
    # if there are no elements in the list
    if (not unSortedLst ):
        return unSortedLst
    # create a treeNode
     root = TreeNode(unSortedLst[0])
    # keep on inserting to the tree
    for i in range ( 1,len(unSortedLst)):
        insertIntoBST(root,unSortedLst[i])

    # now use inorder traversal to put in order
    rtlist = []
    inorder(root,rtlist)
    return rtlist






