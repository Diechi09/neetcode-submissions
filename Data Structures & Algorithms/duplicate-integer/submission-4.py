class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = set()
        for i in range(len(nums)):
            if nums[i] not in answer:
                answer.add(nums[i])
            else:
                return True
        return False

        