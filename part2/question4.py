# Avl methods implemention methods
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.height = 0
def height(root):
    if root == None:
        return 0
    return root.height
# recurisve function

def bf ( root):
    # this is a helper function that returns the bf factor
    leftH = 0
    rightH = 0
    if root == None:
        return 0
    if root.left != None:
        leftH = root.left.height
    if root.right !=None:
        rightH = root.right.height

    return leftH - rightH

# helper method for insert
def rightRotate(head):
    left = head.left
    leftRight = left.right
    left.right = head
    head.left= leftRight
    # update height
    head.height = max(height(head.left),height(head.right)) +1
    left.height = max(height(left.left),height(left.right)) +1

    return left

    # left is the new head now

# change the method to avoid plagerisum
def leftRotate( z):
    y = z.right
    T2 = y.left
    # Perform rotation
    y.left = z
    z.right = T2
    # update the height
    z.height = max(height(z.left), height(z.right)) + 1
    y.height = max(height(y.left),height(y.right))+1
    return y

# min max also same as bst impl

def pred(root):
    # intertive
    while (root.right != None):
        root = root.right
    return root


def succ(root):
    while (root.left != None):
        root = root.left
    return root
# Itertive find next and find prev - these are not different then bst

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




def getParrent(masterRoot,child):
    """ helper method that gets parrent for bubbleUP
    :rtype TreeNode()
    """
    rootP =None
    current= masterRoot
    if masterRoot == None or child == None:
        print("returning null")
        return None
    while ( current != child):

        if child.val <current.val:
            rootP = current
            current = current.left
        elif child.val > current.val:
            rootP = current
            current = current.right
    return rootP


# helper functions for matianing avl
def deleteAvl (root):
    """
    this is a helper function
    :param root:
    :return:
    """
    # todo put all the nodes in a array then you can bubble up
    myNodes = []
    q = [root]
    while not not q:
        node = q.pop(0)
        myNodes.append(node)
        if node != None:
            q.append(node.left)
            q.append(node.right)
    # now go through the array bottom up approach

    for i in range (len(myNodes) -1 , -1 , -1):
        # check the bf factor
        element = myNodes[i]
        if element != None:
            element.height = max(height(element.left),height(element.right))+1
        rootP = element
        if element == None:
            continue
        bfFactor = bf(element)

        # todo add the logic


        if bfFactor >1  and bf(root.left) >=0:
            element = rightRotate(element)
        if bfFactor >1 and bf(root.left) <0:
            element.left = leftRotate(element.left)
            element = rightRotate(element)
        if bfFactor <-1 and bf(element.right) <=0:
            element = leftRotate(element)
        if bfFactor <-1 and bf(element.right) >0:
            element.right = rightRotate(element.right)
            element = leftRotate(element)
    root = element

    return root


def bubbleUp (insertNode,masterNode,val):
    """
    helper method for insert node - it mimics the bubble up like with the recur impl
    :param insertNode:
    :param masterNode:
    :param val:
    :return:
    """
    # val is the inserted val
    # update the heights
    q = [insertNode]
    while not not q:
        nodeQ = q.pop(0)

        # print(nodeQ.val)
        myParrent = getParrent(masterNode,nodeQ)
        # print(myParrent.val)
        # print(myParrent.val)

        bfFactor = bf(nodeQ)


        if bfFactor >= -1 and bfFactor <= 1:
            if myParrent == None:

                return nodeQ
            nodeQ.height = max(height(nodeQ.left), height(nodeQ.right)) + 1
            q.append(myParrent)
            continue
            # now adress the cases

        if bfFactor > 1 and val < nodeQ.left.val:
            if myParrent == None:
                nodeQ = rightRotate(nodeQ)
            elif myParrent.left == nodeQ:
                myParrent.left  = rightRotate(nodeQ)
            else:
                myParrent.right = rightRotate(nodeQ)
        # left rotate
        elif bfFactor < -1 and val > nodeQ.right.val:
            if myParrent == None:
                nodeQ = leftRotate(nodeQ)
            elif myParrent.left == nodeQ:
                myParrent.left = leftRotate(nodeQ)
            else:
                myParrent.right = leftRotate(nodeQ)
            # preOrder(myNode)
        #
        elif bfFactor > 1 and val > nodeQ.left.val:
            nodeQ.left = leftRotate(nodeQ.left)
            if myParrent == None:
                nodeQ = rightRotate(nodeQ)

            elif myParrent.left == nodeQ:
                myParrent.left = rightRotate(nodeQ)
            else:
                myParrent.right = rightRotate(nodeQ)

        elif bfFactor < -1 and val < nodeQ.right.val:
            nodeQ.right = rightRotate(nodeQ.right)
            if myParrent == None:
                nodeQ = leftRotate(nodeQ)
            elif myParrent.left == nodeQ:
                myParrent.left = leftRotate(nodeQ)
            else:
                myParrent.right = leftRotate(nodeQ)
        nodeQ.height = max(height(nodeQ.left), height(nodeQ.right)) + 1
        if myParrent != None:
            q.append(myParrent)
        if myParrent == None:
            # this  is the finished product
            return nodeQ



    # do the bf checking



def iterInsert(node , val):
    # Todo insert the same logic for intertive bst
    newNode = TreeNode(val)
    current = node
    yP = None
    while ( current!=None):
        yP = current
        if val <current.val:
            current = current.left
        else:
            current = current.right
    if yP == None:
        yP = newNode
        node = bubbleUp(newNode, node, newNode.val)
    elif val <yP.val:
        yP.left = newNode
        node = bubbleUp(newNode, node, newNode.val)
    else:
        yP.right = newNode
        node =bubbleUp(newNode,node,newNode.val)
    # once you found the node


    return node

def deleteIter(root , key):
    #todo put itertive delete method
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

        # at this point the node  has been deleted  now buble up
    baseP =deleteAvl(root)
    return baseP


