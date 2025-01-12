class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  
        s.sort() 

        content_children = 0
        child_index = 0
        for cookie_size in s:
            if child_index < len(g) and cookie_size >= g[child_index]:
                content_children += 1
                child_index += 1

        return content_children
