
from question4 import bf,rightRotate,leftRotate,bubbleUp
from question5 import getRandomArray
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getSortedArray (n):
    rtList = []
    for i in range(0,n):
        rtList.append(n-i)
    return rtList
# 6 A **********************************************************

# AVL implementation for levels

def iterInsert(node, val):
    """
    returns the the root and the number of levels
    :param node:
    :param val:
    :return: list[TreeNode,int]
    """
    newNode = TreeNode(val)
    current = node
    rtList = []
    yP = None
    count = 0
    while ( current!=None):
        yP = current
        if val <current.val:
            count +=1
            current = current.left
        else:
            count +=1
            current = current.right
    if yP == None:
        yP = newNode
        node = bubbleUp(newNode, node, newNode.val)
    elif val <yP.val:
        yP.left = newNode
        node = bubbleUp(newNode, node, newNode.val)
    else:
        yP.right = newNode
        node = bubbleUp(newNode, node, newNode.val)
    # once you found the node
    #Todo create helper function
    return [node,count]


# bst implemenation return the  count


def insertIntoBST( root, val):
    """
            :type root: TreeNode
            :type val: int
            :rtype: List[TreeNode,Int]
            """

    # first find where to insert the node
    count = 0
    current = root
    if current == None:
        return None
    while (current != None):

        if current.val > val and current.left != None:
            current = current.left
            count +=1
            continue
        elif current.val < val and current.right != None:
            current = current.right
            count +=1
            continue
        # base cases
        if current.val > val and current.left == None:

            current.left = TreeNode(val)
            break
        elif current.val < val and current.right == None:
            current.right = TreeNode(val)
            break
    return [root,count]

# 6B *****************************************************************************
# goal is to compare the levels -
# hypothiesis Avl will outpreform bst

def levelsCompare(array):
    # myArray = getRandomArray(10000)
    levelAvl = 0
    root = TreeNode(-4)
    count = 0
    for element in array:
        # print(count)
        count +=1
        myList = iterInsert(root,element)
        root = myList[0]
        levelAvl += myList[1]

    count2 = 0
    root2 = TreeNode(-2)
    for e in array:
        myList = insertIntoBST(root2,e)
        root2 = myList[0]
        count2 += myList[-1]
    print(str(count2) + " bst")
    print(str(levelAvl) + "avl")

myList = getRandomArray(10000)
# levelsCompare(myList)
"""
output
161976 bst
121362avl

"""
# 6c remember a sorted in our prev bst algo will form a linked list :( that's not fun!
"""
49995000 bst
123631avl
"""
list2 = getSortedArray(10000)

levelsCompare(list2)







