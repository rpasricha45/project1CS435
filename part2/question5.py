"""
comparing bst and avl preformance enjoy ! test the preformace of the two data structures
"""
import random
from question4 import iterInsert,deleteIter
from BSTInsert import insertIntoBST,recBstInsert

# TODO add more testing to this fucntion


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

def getRandomArray ( n):
    """
    :param n size of random array:
    :return: random array of size n
    """
    # keep track of the number of number elements added
    numbElements = 0
    # create a set to keep track of unique elements
    mySet = set ()

    rtList = []

    while (numbElements<n):
        # Todo use random int https://www.geeksforgeeks.org/python-randint-function/
        r1 = random.randint(0, n*2)
        if r1 not in mySet:
            rtList.append(r1)
            numbElements +=1
            mySet.add(r1)
    return rtList

# 5A - I did not implement the recursive avl - for extra credit but I  will test the rec bst
# I am going to use sorted Array - worst case is much worse for bst better to test - this will cause a issue - for recursion ! But this a good thing!
def recursive ():
    myArray = getSortedArray(10000)
    root = TreeNode(-2)
    for element in myArray:
        # monitor if the proccess is still running
        print("running - ")
        recBstInsert(root,element)
# I commented out - it will crash the code ! - b/c recursion depth
# recursive()

# Question 5 C test the IterMethods
def Iteritive ( nElements):
    myArray = getRandomArray(nElements)
    root = TreeNode(-2)

    count = 0
    for element in myArray:
        # monitor if the proccess is still running
        if count % 10 == 0:
            print("running")
        root = insertIntoBST(root, element)
    root2 = TreeNode(-3)
    count = 0
    for k in myArray:
        if count % 10 == 0:
            print("running")
        count +=1
        root2 = iterInsert(root2, k)


Iteritive(10000)







