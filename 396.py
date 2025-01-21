class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))  
        max_value = F

        for k in range(1, n):
            F += sum_nums - n * nums[-k]
            max_value = max(max_value, F)

        return max_value
