class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(bobValues)
        combined = [(aliceValues[i] + bobValues[i], i) for i in range(n)]
        combined.sort(reverse=True, key=lambda x: x[0])
        #print(combined) -- keep the index of the stone
        #maximum aliceValues[i] + bobValues[i]

        alice_score, bob_score = 0, 0
        for turn, (_, idx) in enumerate(combined):
            if turn % 2 == 0:  
                alice_score += aliceValues[idx]
            else:  
                bob_score += bobValues[idx]
        
        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0
