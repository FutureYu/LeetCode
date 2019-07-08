class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0 or numRows == 0 or numRows == 1:
            return s
        res = ""
        totalSize = len(s)
        size = 2 * numRows - 2
        for i in range(numRows):
            for j in range(totalSize//size + 1):
                if (j * size + i < totalSize):
                    res += s[j * size + i]
                if not (i == 0 or i == numRows - 1):
                    spe = j * size + i + 2 * (numRows - 1 - i)
                    if spe < totalSize:
                        res += s[j * size + i + 2 * (numRows - 1 - i)]
        return res
if __name__ == "__main__":
    print(Solution.convert(Solution, "ABABAB", 2))