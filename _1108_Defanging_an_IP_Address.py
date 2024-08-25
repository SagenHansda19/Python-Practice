class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for i in range(0,len(address)):
            if address[i] == '.':
                res += "[.]"
            else:
                res += address[i]
        return res
address = "1.1.1.1"
sol1 = Solution()
sol11 = sol1.defangIPaddr(address)
print(sol11)