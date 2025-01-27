class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        max_h_gap = 0
        current_h_gap = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i-1]+1:
                current_h_gap += 1
            else:
                max_h_gap = max(max_h_gap, current_h_gap)
                current_h_gap = 1
        max_h_gap = max(max_h_gap, current_h_gap)

        max_v_gap = 0
        current_v_gap = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i-1]+1:
                current_v_gap += 1
            else:
                max_v_gap = max(max_v_gap, current_v_gap)
                current_v_gap = 1
        max_v_gap = max(max_v_gap, current_v_gap)

        return min(max_h_gap+1, max_v_gap+1)**2
