class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        result = 0

        if k == 0:
            result = sum(1 for num in count if count[num] > 1)
        else:
            result = sum(1 for num in count if num + k in count)

        return result
