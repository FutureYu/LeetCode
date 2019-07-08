class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = []
        for k in range(len(s)):
            p.append([False] * len(s))
        # 先初始化长度为 0 时的结果
        for k in range(1, len(s)):
            p[k][k - 1] = True
        for k in range(len(s)):
            # 最多只有 len(s) 次遍历，第 k 次遍历长度为 k + 1 的字符串
            # p(i, i + k) = p (i + 1, i + k - 1) && s(i) == s(i + k)
            # k 为 0 时，直接初始化为 True
            for i in range(0, len(s) - k):
                if k == 0:
                    p[i][i + k] = True
                else:
                    p[i][i + k] = p[i + 1][i + k - 1] and s[i] == s[i + k]

        # 找出最长回文子序列
        maxi = 0
        maxj = 0
        maxLen = -1
        for i in range(len(s)):
            for j in reversed(range(len(s))):
                if p[i][j] == True and j - i >= maxLen:
                    maxLen = j - i
                    maxi = i
                    maxj = j
                    break
        return s[maxi: maxj + 1]

if __name__ == "__main__":
    print(Solution.longestPalindrome(Solution, "1111"))


