class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i and a == nums[i-1]:
                continue

            left = i + 1
            rigth = len(nums) - 1

            while left < rigth:
                three_sum = a + nums[left] + nums[rigth]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    rigth -= 1
                else:
                    result.append([a, nums[left], nums[rigth]])
                    left += 1
                    while left < rigth and nums[left] == nums[left - 1]:
                        left += 1

        return result


