class Solution:
    def reverse(self, x: int) -> int:
        MAX = pow(2, 31)
        ans = 0
        if x >= 0:
            while x != 0:
                pop = x % 10
                if ans > (MAX - 1) // 10 or (ans == (MAX - 1) // 10 and pop > 7):
                    return 0
                ans = ans * 10 + pop
                x //= 10
            return ans
        else:
            x = -x
            while x != 0:
                pop = x % 10
                if ans > MAX // 10 or (ans == MAX // 10 and pop > 8):
                    return 0
                ans = ans * 10 + pop
                x //= 10
            return -ans
if __name__ == "__main__":
    print(Solution.reverse(Solution, -123))
