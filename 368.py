class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)

        dp = [1] * n
        prev_index = [-1] * n

        max_length = 1
        max_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev_index[i] = j
                    if dp[i] > max_length:
                        max_length = dp[i]
                        max_index = i

        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev_index[max_index]

        return result[::-1]
