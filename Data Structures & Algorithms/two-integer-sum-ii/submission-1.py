class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            usum = numbers[l] + numbers[r]
            if usum == target:
                return [l + 1, r + 1]
            if usum < target:
                l += 1
                while numbers[l] == numbers[r]:
                    l += 1
            else:
                r -= 1
                while numbers[l] == numbers[r]:
                    r -= 1
        return []