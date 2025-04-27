# candies = [2,3,5,1,3], extraCandies = 3
# candies's Max: 5
# 2+3 >= 5 True
# 3+3 >= 5 True
# 5+3 >= 5 True
# 1+3 >= 5 False
# 3+3 >= 5 True

from typing import List

# Time Complexity: O(n)
def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    result = []
    i = 0
    _max = max(candies)

    while i < len(candies):
        if candies[i] + extraCandies >= _max:
            result.append(True)
        else: 
            result.append(False)
        i += 1 
    return result

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))

candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))

candies = [12,1,12]
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))
