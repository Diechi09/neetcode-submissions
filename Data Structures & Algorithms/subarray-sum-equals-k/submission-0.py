class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cursum = 0
        prefix = {0:1}
        for n in nums:
            cursum += n
            difference = cursum - k
            ans += prefix.get(difference, 0)
            prefix[cursum] = 1 + prefix.get(cursum, 0)
        return ans