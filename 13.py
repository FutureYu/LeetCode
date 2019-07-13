class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 0
        if "IV" in s:
            res += 4
            s = s.replace("IV", "")
        if "IX" in s:
            res += 9
            s = s.replace("IX", "")
        if "XL" in s:
            res += 40
            s = s.replace("XL", "")
        if "XC" in s:
            res += 90
            s = s.replace("XC", "")
        if "CD" in s:
            res += 400
            s = s.replace("CD", "")
        if "CM" in s:
            res += 900
            s = s.replace("CM", "")
        res += 1 * s.count("I")
        res += 5 * s.count("V")
        res += 10 * s.count("X")
        res += 50 * s.count("L")
        res += 100 * s.count("C")
        res += 500 * s.count("D")
        res += 1000 * s.count("M")
        return res

if __name__ == "__main__":
    print(Solution.romanToInt(Solution, "LVIII"))