"""
LeetCode 373. Find K Pairs with Smallest Sums
blog : https://daimhada.tistory.com/51
problem : https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
"""
import itertools

def kSmallestPairs(nums1, nums2, k):
    Pairs = []
    for com in itertools.product(*[nums1, nums2]):
        sumCom = sum(com)
        Pairs.append([com, sumCom])
    Pairs.sort(key=lambda item:item[1])
    Pairs = Pairs[:k]
    return [pair[0] for pair in Pairs]

kSmallestPairs([1,2,4,5,6],[3,5,7,9], 3) # [[1,3],[2,3],[1,5]]
kSmallestPairs([1,7,11],[2,4,6], 3) # [[1,2],[1,4],[1,6]]
kSmallestPairs([1,1,2],[1,2,3], 2) # [1,1],[1,1]
kSmallestPairs([1,2],[3], 3) # [1,3],[2,3]
