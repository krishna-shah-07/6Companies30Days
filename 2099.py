class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_arr = [(value, index) for index, value in enumerate(nums)]
        indexed_arr.sort(key=lambda x: x[0], reverse=True)

        top_k = indexed_arr[:k]
        top_k.sort(key=lambda x: x[1])

        result = [value for value, index in top_k]
        return result
