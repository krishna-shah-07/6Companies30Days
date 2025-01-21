class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        prev = [0] * (n + 1)
        max_length = 0

        for i in range(m - 1, -1, -1):
            curr = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    curr[j] = prev[j + 1] + 1
                    max_length = max(max_length, curr[j])
            prev = curr

        return max_length
