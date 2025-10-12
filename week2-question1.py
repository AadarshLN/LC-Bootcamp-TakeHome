class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        while i < n and s[i] == ' ' :
            i += 1
        
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            else:
                sign = 1
            i += 1
        
        result = 0

        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        if result*sign > 2**31 - 1:
            return 2**31-1
        if result * sign < -2**31:
            return -2**31

        return result * sign


       
        
