class Solution:
    def compress(self, chars: List[str]) -> int:
        n = 1
        result = []
        leng = len(chars)

        if leng == 1:
            return 1

        for i in range(leng - 1):
            if chars[i] == chars[i + 1]:
                n += 1
            else:
                result.append(chars[i])
                if n > 1:
                    result.extend(list(str(n)))
                n = 1
        
        result.append(chars[-1])
        if n > 1:
            result.extend(list(str(n)))
        
        for i in range(len(result)):
            chars[i] = result[i]

        return len(result)
        
