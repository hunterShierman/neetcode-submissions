class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        n = len(nums)
        bucket = []
        output = []
        count = 0

        for i in range(n + 1):
            bucket.append([] )
        
        # find freq of each unique element using dict
        for i in range(n):
            if nums[i] in map:
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1

        # use bucket sort
        for key in map:
            bucket[map[key]].append(key)

        # add the k largest elements
        for i in range(len(bucket) -1, -1, -1):
            if count >= k:
                break

            if bucket[i] != []:
                output += bucket[i]
                count += len(bucket[i])

        return output

        






        

            

