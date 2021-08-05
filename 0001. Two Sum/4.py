#60ms

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            if target - n in nums_map:
                return [nums_map[target - n], i]
            nums_map[n] = i
