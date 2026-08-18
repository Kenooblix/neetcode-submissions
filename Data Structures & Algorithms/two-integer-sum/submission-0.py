class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counterpart = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in counterpart:
                return [counterpart[rest], i]
            counterpart[nums[i]] = i