class Solution:
    def reverseWords(self, s: str) -> str:
        rev = ""
        s = s.strip().split()
        for i in range(len(s)-1,-1,-1):
            rev += s[i]
            if i != 0:
                 rev += " "

        return rev
