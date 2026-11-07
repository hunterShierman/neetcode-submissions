class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        comparisonArr = []
        nums.sort()
        for i in range(len(nums)):
            comparisonArr.append(i)

        for i in range(len(nums)):
            if nums[i] != comparisonArr[i]:
                return comparisonArr[i]

        print(nums)
        print(comparisonArr)
        return len(nums)