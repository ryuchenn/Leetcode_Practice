from typing import List

# Time Complexity: O(n)
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    flowerbed = [0] + flowerbed + [0]
    _len = len(flowerbed)
    i = 1
    
    while i < _len-1:
        if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        if n<=0: 
            return True 
        i += 1 
    return False


flowerbed = [1,0,0,0,1]
n = 1 # true
print(canPlaceFlowers(flowerbed, n))

flowerbed = [1,0,0,0,1]
n = 2 # false
print(canPlaceFlowers(flowerbed, n))

flowerbed = [1,0]
n = 1 # false
print(canPlaceFlowers(flowerbed, n))