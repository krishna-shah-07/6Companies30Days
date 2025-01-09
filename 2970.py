class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for start in range(n):
            for end in range(start, n):
                before = nums[:start]
                after = nums[end+1:]
                modified = before + after

                if all(modified[i] < modified[i+1] for i in range(len(modified)-1)):
                    count += 1

        return count
