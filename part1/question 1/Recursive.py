# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# the methods will be listed   underneth - pleas make sure to look at testing folder to see preformance  specs
# Todo create helper methods for delete bst  - these methods are synomous to max and min

def pred( root):
    if root == None:
        return None
    if root.right == None:
        return root
    return pred(root.right)
def succ ( root):
    if root == None:
        return None
    if root.left == None:
        return root
    return succ(root.left)

# delete bst
 def deleteNode(self, root, key):

        if root == None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        else:
            if root.left == None and root.right == None:
                root = None
            elif root.left != None and root.right == None:
                node = pred(root.left)
                root.val = node.val
                root.left = self.deleteNode(root.left, root.val)
            else:
                myNode = succ(root.right)
                root.val = myNode.val
                root.right = self.deleteNode(root.right, root.val)
        return root

# This is the helper method to insert method

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


 def insertBst( root,val):
     helper(root,val)
     return root


 # find next and find min

 def findNext (rootN , parrent,val):
     # given a node find the next -
     if rootN == None:
         return None

     if rootN.val > val:
         findNext(rootN.left , rootN,val)
     elif rootN.val < val:
         findNext(rootN.right , rootN,val)

     else:
         # edge case 1 if there is a right child
         if rootN.right != None:
             # find the min element to the right
            return succ(rootN.right)
         # if there is not a right node but there is a parrent just return the the parrent
         elif rootN != parrent:
             return parrent
         # edge case if there is only something to the left - there is nothing to the left
         else:
             return None
def findPrev ( rootN, parrent , val):
    #Todo first find the node
    if rootN.val >val:
        findPrev(rootN.left , rootN, val)
    elif rootN.val < val:
        findPrev(rootN.right, rootN,val)
    else:
        if rootN.left != None:
            return pred(rootN.left)
        # edge case if there is not a  left node return parent
        elif rootN != parrent:
            return parrent
        else:
            return None




