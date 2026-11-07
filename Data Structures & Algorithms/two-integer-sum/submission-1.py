class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numsSeen = {}
        # [key, value]

        for i in range(len(nums)) :

            target2 = target - nums[i]
            if target2 in numsSeen:
                return [numsSeen[target2], i]
            numsSeen[nums[i]] = i

        return []
         