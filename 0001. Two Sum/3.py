#56ms

def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, n in enumerate(nums):
        nums_map[n] = i

    for i, n in enumerate(nums):
        if target - n in nums_map and i != nums_map[target - n]:
            return [i, nums_map[target - n]]
