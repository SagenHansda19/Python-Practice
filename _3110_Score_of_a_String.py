class Solution:
    def scoreOfString(self, s: str) -> int:
        # n = len(s)
        score : int = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i-1]))
            
        # for i in range(1,n):
        #     score += abs(ord(s[i]) - ord(s[i-1]))

        # for i in range(0,n-1,2):
        #     score += abs(ord(s[i]) - ord(s[i+1]))
        # for i in range(1,n-1,2):
        #     score += abs(ord(s[i]) - ord(s[i+1]))
        return score