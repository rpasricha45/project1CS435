"""
(You must submit code for this question! ) Implement a function getSortedArray(n)
where the output is an array of size n. The 0th element should be equal to n, the
1st element should be equal to n-1, and so on.
"""


"""
Assume - sotedt order
if n = 0 return empty array
n >=0


input  { 0,1,2,3}
output {4,3,2,1}
"""
def getSortedArray (n):
    rtList = []
    for i in range(0,n):
        rtList.append(n-i)
    return rtList