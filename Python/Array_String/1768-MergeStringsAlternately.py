from functools import reduce
from itertools import zip_longest

# Time Complexity: O((m+n)^2)
def mergeAlternately1(word1: str, word2: str) -> str:
    return ''.join(reduce(lambda a, b: a+b, zip_longest(word1, word2, fillvalue='')))

# Time Complexity: O((m+n))
def mergeAlternately2(word1: str, word2: str) -> str:
    result = []
    i, j = 0,0

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            result.append(word1[i])
            i+=1
        if j < len(word2):
            result.append(word2[j])
            j+=1
    
    return ''.join(result)

word1 = "abc"
word2 = "pqr"
# print(mergeAlternately1(word1, word2))
# print(mergeAlternately2(word1, word2))

word1 = "ab"
word2 = "pqrs"
# print(mergeAlternately1(word1, word2))
# print(mergeAlternately2(word1, word2))

word1 = "abcd"
word2 = "pq"
# print(mergeAlternately1(word1, word2))
# print(mergeAlternately2(word1, word2))
