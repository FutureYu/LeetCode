class Solution:
    def intToRoman(self, num: int) -> str:
        if not (1 <= num <= 3999):
            return ""
        res = ""
        ge = num % 10
        shi = num // 10 % 10
        bai = num // 100 % 10
        qian = num // 1000 % 10
        res += "M" * qian

        if bai == 4:
            res += "CD"
        elif bai == 9:
            res += "CM"
        elif bai >= 5:
            res += "D"
            bai -= 5
        if bai <= 3:
            res += "C" * bai

        if shi == 4:
            res += "XL"
        elif shi == 9:
            res += "XC"
        elif shi >= 5:
            res += "L"
            shi -= 5
        if shi <= 3:
            res += "X" * shi

        if ge == 4:
            res += "IV"
        elif ge == 9:
            res += "IX"
        elif ge >= 5:
            res += "V"
            ge -= 5
        if ge <= 3:
            res += "I" * ge
        return res


if __name__ == "__main__":
    print(Solution.intToRoman(Solution, 1994))
