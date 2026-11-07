class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:\

        # inital thoughts
        # create a dictionary with key values
        # add each num to dict
        # check before you add a number if it is already in there if it is there is a duplicate

        numDict = {}
        duplicate = False
        
        # add each num to dict
        for num in nums:

            # if its already in there duplicate therefore false
            if num in numDict:
                duplicate = True
                break
            # if its not in there add it to the dict
            else:
                numDict[num] = 1

        return duplicate
                
