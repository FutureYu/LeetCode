class Solution:
    def maxArea(self, height) -> int:
        if len(height) <= 1:
            return 0
        i = 0
        j = len(height) - 1
        max = 0
        while i < j:
            b = j - i
            if height[i] < height[j]:
                a = height[i]
                i += 1
            else:
                a =  height[j]
                j -= 1
            max = max if a * b < max else a * b

        return max


if __name__ == "__main__":
    print(Solution.maxArea(Solution, [1]))
