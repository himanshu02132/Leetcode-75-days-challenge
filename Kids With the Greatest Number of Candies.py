class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = max(candies)
        result =[]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= x:
                result.append(True)
            else:
                result.append(False)

        return result
