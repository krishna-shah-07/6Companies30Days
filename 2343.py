class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        for place, trim in queries:
            tempnums = []
            for i in range(len(nums)):
                tempnums.append((nums[i][-trim:], i))
            tempnums.sort()
            res.append(tempnums[place-1][1])
        
        return res
