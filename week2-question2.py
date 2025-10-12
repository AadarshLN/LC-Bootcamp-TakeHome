class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p) #window size
        n = len(s)
        indices = []
        frequencies = defaultdict(int)
        if p > s:
            return indices
        for char in p:
            frequencies[char] += 1
        
        for i in range(m-1):
            if s[i] in frequencies:
                frequencies[s[i]] -=1 
        
        for i in range(-1,n-m+1):
            if i>-1 and s[i] in frequencies:
                frequencies[s[i]] += 1
            if i+m < n and s[i+m] in frequencies:
                frequencies[s[i+m]] -= 1

            if not any(frequencies.values()):
                indices.append(i+1)
        return indices
        
