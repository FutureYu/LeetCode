class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        res = 0
        # 1221
        while x > res:
            res *= 10
            res += x % 10
            x //= 10
        if x == res or x == res // 10:
            return True
        return False

if __name__ == "__main__":
    print(Solution.isPalindrome(Solution, 1230))
