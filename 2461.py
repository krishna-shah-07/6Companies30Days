class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0

        # res = 0
        # for i in range(n-k+1):
        #     if len(nums[i:i+k]) == len(set(nums[i:i+k])):
        #         res = max(res, sum(nums[i:i+k]))

        window_sum = 0
        element_count = defaultdict(int)
        max_sum = 0
        left = 0

        for right in range(n):
            window_sum += nums[right]
            element_count[nums[right]] += 1

            if right - left + 1 > k:
                window_sum -= nums[left]
                element_count[nums[left]] -= 1
                if element_count[nums[left]] == 0:
                    del element_count[nums[left]]
                left += 1

            if right - left + 1 == k and len(element_count) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum
