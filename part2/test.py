"""
Testing  for functions
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.height = 0

from avl import iterInsert,deleteIter

print("starting test")



# geeks for geeks preorder method
def preOrder(root):
    if not root:

        return

    print("{0} ".format(root.val), end="")
    preOrder(root.left)
    preOrder(root.right)


# geeks for geeks test
def insertTest ():
    root = TreeNode(10)

    myData = [20,30,40,50,25]
    for test in myData:
        # print("inserting " + str(test))
        root =iterInsert(root,test)


    preOrder(root)




# insertTest()



# geeks for geeks test
def deleteTest ():
    root = TreeNode(9)
    myData = [5,10,0,6,11,-1,1,2]
    for test in myData:
        root = iterInsert(root,test)
    root = deleteIter(root,10)
    preOrder(root)


deleteTest()