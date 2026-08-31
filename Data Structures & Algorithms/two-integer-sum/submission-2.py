class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         prevMap = {}

         for i, n in enumerate(nums):
            desire = target - n
            if desire in prevMap:
                return [prevMap[desire],i]
            prevMap[n] = i