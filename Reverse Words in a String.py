class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.split()
        s2 = s1[::-1] 
        return " ".join(s2)
