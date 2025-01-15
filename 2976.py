class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[math.inf] * 26 for _ in range(26)]
        for i in range(26):
            graph[i][i] = 0 
        
        for o, c, z in zip(original, changed, cost):
            graph[ord(o) - ord('a')][ord(c) - ord('a')] = min(graph[ord(o) - ord('a')][ord(c) - ord('a')], z)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            cost = graph[ord(s) - ord('a')][ord(t) - ord('a')]
            if cost == math.inf: 
                return -1
            total_cost += cost
        
        return total_cost
