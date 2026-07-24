class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        ans = []
        for num in nums:
            res[num] = res.get(num, 0) + 1
        sortedlist = sorted(res, key=res.get, reverse=True)
        for i in range(k):
            ans.append(sortedlist[i])
        return ans