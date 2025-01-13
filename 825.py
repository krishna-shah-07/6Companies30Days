class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = Counter(ages)  
        res = 0
        
        for age_x in count:
            for age_y in count:
                if age_y <= 0.5 * age_x + 7:  
                    continue
                if age_y > age_x:  
                    continue
                if age_y > 100 and age_x < 100: 
                    continue
                
                if age_x == age_y:
                    res += count[age_x] * (count[age_x] - 1) 
                else:
                    res += count[age_x] * count[age_y]
        
        return res
