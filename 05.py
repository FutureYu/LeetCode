class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size == 0:
            return s
        p = []
        res = s[0]
        maxLen = -1
        for k in range(size):
            p.append([-1] * size)
        # 先初始化长度为 0 时的结果
        for k in range(1, size):
            p[k][k - 1] = 0
        for k in range(size):
            # 最多只有 size 次遍历，第 k 次遍历长度为 k + 1 的字符串
            # p 存放长度
            # p(i, i + k) = p (i + 1, i + k - 1) && s(i) == s(i + k)
            # k 为 0 时，直接初始化为 1
            for i in range(0, size - k):
                if k == 0:
                    p[i][i + k] = 1
                else:
                    if p[i + 1][i + k - 1] != -1 and s[i] == s[i + k]:
                        p[i][i + k] = p[i + 1][i + k - 1] + 1
                        if maxLen <= p[i + 1][i + k - 1] + 1:
                            maxLen = p[i + 1][i + k - 1] + 1
                            res = s[i: i + k + 1]
                    else:
                        p[i][i + k] = -1
        return res

if __name__ == "__main__":
    print(Solution.longestPalindrome(Solution, "asasdas"))