from math import gcd

# Time Complexity: O(m+n)
def gcdOfStrings1(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    leng = gcd(len(str1), len(str2))
    return str1[:leng]
    
def gcdOfStrings2(str1: str, str2: str) -> str:
    def my_gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a
    if str1 + str2 != str2 + str1:
        return ""
    leng = my_gcd(len(str1), len(str2))
    return str1[:leng] 

str1 = "ABCABC"
str2 = "ABC"
# print(gcd(len(str1), len(str2)))
print(gcdOfStrings1(str1, str2))

str1 = "ABABAB"
str2 = "ABAB"
print(gcdOfStrings1(str1, str2))


str1 = "LEET"
str2 = "CODE"
print(gcdOfStrings1(str1, str2))
