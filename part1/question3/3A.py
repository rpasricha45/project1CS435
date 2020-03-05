"""
This is random  get randomArray (n)
Implement a function getRandomArray(n)
where the output is an array of size n, and contains distinct random numbers (in
other words, no two numbers in the array should be the same number). Math.rand()
might be useful here.
"""
import random

# TODO add more testing to this fucntion
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
