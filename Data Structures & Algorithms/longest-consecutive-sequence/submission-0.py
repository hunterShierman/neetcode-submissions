class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        loop = True
        i = 1
        maxSeq = 0
        currSeq = 1

        if len(nums) > 0:
            maxSeq = 1

        while loop is True and i < len(nums):

            if nums[i] == nums[i - 1]:
                i += 1
                continue

            if nums[i] == nums[i - 1] + 1:
                currSeq += 1

                if currSeq > maxSeq:
                    maxSeq = currSeq 

            else:
                currSeq = 1

            i += 1

        return maxSeq
            

