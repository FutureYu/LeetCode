class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = ""
        if len(strs) == 0:
            return ""
        minLen = 0xFFFFFFFF
        for s in strs:
            if len(s) == 0:
                return ""
            if len(s) < minLen:
                minLen = len(s)
        i = 0
        while i < minLen:
            c = strs[0][i]
            for s in strs:
                if c != s[i]:
                    return res
            res += c
            i += 1
        return res
                

if __name__ == "__main__":
    print(Solution.longestCommonPrefix(Solution, ["", "sfaf"]))