class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            r = columnNumber % 26
            res.append(chr(int(r) + ord('A')))
            columnNumber //= 26

        return ''.join(reversed(res))
