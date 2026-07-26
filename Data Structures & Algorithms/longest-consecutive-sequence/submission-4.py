class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for i in range(len(nums)):
            current = nums[i]
            length = 0
            if current - 1 in numbers:
                continue
            while (current + length) in numbers:
                length += 1
            longest = max(longest, length)
        return longest


