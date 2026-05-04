class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a','e','i','o','u', 'A','E','I','O','U']
        x = []
        for i in range(len(s)):
            if s[i] in v:
                x.append(s[i])

        chars = list(s)
        n = len(x)
        for i in range(len(chars)):
            if chars[i] in v:
                chars[i] = x[n-1]
                n = n-1
        return "".join(chars)
