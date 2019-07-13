class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

print(Solution.defangIPaddr(Solution, "192.168.2.1"))