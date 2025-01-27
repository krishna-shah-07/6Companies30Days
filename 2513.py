class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b

        def is_feasible(max_val):
            divisible_by_div1 = max_val // divisor1
            divisible_by_div2 = max_val // divisor2
            divisible_by_both = max_val // lcm(divisor1, divisor2)

            not_div1 = max_val - divisible_by_div1
            not_div2 = max_val - divisible_by_div2
            not_either = max_val - (divisible_by_div1 + divisible_by_div2 - divisible_by_both)

            if not_div1 < uniqueCnt1 or not_div2 < uniqueCnt2:
                return False
            return not_div1 + not_div2 - not_either >= uniqueCnt1 + uniqueCnt2

        left, right = uniqueCnt1 + uniqueCnt2, 10**18
        while left < right:
            mid = (left + right) // 2
            if is_feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
