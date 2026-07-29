class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        nums = set()
        l = 0
        ans = 0

        for r in range(len(s)):
            while s[r] in nums:
                nums.remove(s[l])
                l += 1
            nums.add(s[r])
            ans = max(ans, r - l + 1)
        return ans