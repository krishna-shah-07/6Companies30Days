class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        heights = [h for _, h in envelopes]
        lis = []  
        for h in heights:
            pos = bisect.bisect_left(lis, h)
            if pos == len(lis):
                lis.append(h)
            else:
                lis[pos] = h
        
        return len(lis)
