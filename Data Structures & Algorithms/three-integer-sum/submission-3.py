class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)):
            # skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # no triplet can sum to 0 if the smallest number is positive
            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicate values for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return output
