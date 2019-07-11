class Solution:
    def myAtoi(self, s: str) -> int:
        MAX = pow(2, 31)
        size = len(s)
        if size == 0:
            return 0
        negetive = "no"
        i = 0
        res = ""
        while i < size:
            if negetive == "no":
                if s[i] == "-":
                    negetive = s[i]
                    i += 1
                    continue
                if s[i] == "+":
                    negetive = ""
                    i += 1
                    continue
                elif s[i].isdecimal(): 
                    negetive = ""
                elif s[i] == " ":
                    i += 1
                    continue
                else:
                    return 0
            if s[i].isdecimal():
                res += s[i]
                i += 1
            else:
                break
        if res == "":
            return 0
        ans = 0
        if negetive == "":
            for i in range(len(res)):
                pop = int(res[i])
                if ans > (MAX - 1) // 10 or (ans == (MAX - 1) // 10 and pop > 7):
                    return MAX-1
                ans = ans * 10 + pop
            return ans
        elif negetive == "-":
            for i in range(len(res)):
                pop = int(res[i])
                if ans > MAX // 10 or (ans == MAX // 10 and pop > 8):
                    return -MAX
                ans = ans * 10 + pop
            return -ans
        else:
            return 0

if __name__ == "__main__":
    print(Solution.myAtoi(Solution, " "))