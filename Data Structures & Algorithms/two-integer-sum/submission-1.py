class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
            seen = dict()

            for i in range(0, len(nums)):
                complement = target - nums[i]
                if complement in seen:
                    return [seen[complement], i]
                else:
                    seen[nums[i]] = i

            return[]