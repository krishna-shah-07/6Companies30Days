class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        slots = 1  # Start with one slot for the root
        
        for node in nodes:
            slots -= 1  # Each node consumes one slot
            if slots < 0:
                return False  # Invalid if slots go negative
            
            if node != '#':  # Non-null nodes create two new slots
                slots += 2
        
        return slots == 0
