# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# the methods will be listed   underneth - pleas make sure to look at testing folder to see preformance  specs
# Todo create helper methods for delete bst  - these methods are synomous to max and min
def pred( root):
    while root.right != None:
        root = root.right
    return root
def succ ( root):
    while root.left != None:
        root = root.left
    return root

# delete bst
# TODO 64/80 test cases itertive
def deleteNode(self, root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
    baseP = root
    # first find the root
    myList = []
    myList.append(root)
    parrent = root
    while (len(myList) > 0):
        testRoot = myList.pop(0)

        if testRoot == None:
            return baseP

        elif testRoot.val > key:
            parrent = testRoot
            myList.append(testRoot.left)

        elif testRoot.val < key:
            parrent = testRoot
            myList.append(testRoot.right)
        elif testRoot.val == key:

            # you found the node
            if testRoot.left == None and testRoot.right == None:
                if testRoot == parrent:
                    return None
                if parrent.left == testRoot:
                    parrent.left = None
                else:
                    parrent.right = None
                return baseP

            elif testRoot.left != None and testRoot.right == None:
                # you need to find the predessor
                myRoot = pred(testRoot.left)
                testRoot.val = myRoot.val
                # todo now you need to delete the root you need to fix

                current = testRoot.left
                parrent = testRoot
                while (current.right != None):
                    parrent = current
                    current = current.right
                parrent.left = None

            else:

                myRoot = succ(testRoot.right)
                testRoot.val = myRoot.val
                # todo you may need to fix this section
                current = testRoot.right
                parrent = testRoot
                while (current.left != None):
                    parrent = current
                    current = current.left
                parrent.right = None
    return baseP


# This is the helper method to insert method

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




    # find next and find min

def binarySearch ( root , val):
    # helper function that returns the root once it finds it along with parrent
    # rtType = lst
    rtList = []
    parrent = root
    while ( root != None):
        if root.val < val:
            parrent = root
            root = root.right
        elif root.val > val:
            parrent = root
            root = root.left
        else:
            # i found the  node
            rtList.append(root)
            rtList.append(parrent)
            break
    return rtList

def findNext ( root , val):
    # iter

    rootList = binarySearch(root,val)
    # I now have the root and the parrent
    # test case 1  if there is a right child
    if rootList[0].right != None:
        return succ(rootList[0].right)
    # if there no right but there is a parrent
    elif rootList[0] != rootList[1]:
        return rootList[1]
    else:
        return None


def findPrev ( root , val):
    rootList = binarySearch(root,val)
    if ( rootList[0].left != None):
        return pred(rootList[0].left)
    # edge case 2 if there is no left but there is a parrent
    # TODO this may not work ! - this logic may be faulty
    elif rootList[0] != rootList[1]:
        return rootList[1]
    else:
        return None







